"""Bounded MCP host. The browser never receives approval signing keys."""
import asyncio
import json
import os
import secrets
import sys
from contextlib import AsyncExitStack, asynccontextmanager
from pathlib import Path
from email.message import EmailMessage
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel, Field
from typing import Literal
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from core import ROOT, FIXTURE, make_plan, load_plan, issue_approval, outputs, ledger, audit

class MCPHost:
    def __init__(self): self.sessions={}; self.trace=[]
    async def start(self,stack):
        os.environ.setdefault('RR_APPROVAL_KEY',secrets.token_hex(32))
        for role in ['evidence','calendar','actions']:
            env={**os.environ}
            # Read-only services don't receive the signing key.
            if role!='actions': env.pop('RR_APPROVAL_KEY',None)
            io=await stack.enter_async_context(stdio_client(StdioServerParameters(command=sys.executable,args=[str(ROOT/'mcp_service.py'),role],env=env)))
            session=await stack.enter_async_context(ClientSession(*io))
            init=await session.initialize()
            found=await session.list_tools()
            self.sessions[role]=session
            self.trace.append({'server':role,'method':'initialize + tools/list','tools':[t.name for t in found.tools],'protocol':init.protocolVersion})
    async def call(self,role,name,args):
        r=await self.sessions[role].call_tool(name,args)
        # Never log approval tokens or full receipt bodies.
        self.trace.append({'server':role,'method':'tools/call','tool':name,'ok':not r.isError})
        self.trace=self.trace[-80:]
        if r.isError: raise ValueError(' '.join(c.text for c in r.content if c.type=='text'))
        if r.structuredContent:
            v=r.structuredContent
            return v.get('result',v)
        texts=[c.text for c in r.content if c.type=='text']
        return json.loads(texts[0])

host=MCPHost()
@asynccontextmanager
async def lifespan(app):
    async with AsyncExitStack() as stack:
        await host.start(stack)
        yield

app=FastAPI(title='ReturnRelay local MCP demo',lifespan=lifespan)
app.add_middleware(TrustedHostMiddleware,allowed_hosts=['127.0.0.1','localhost','testserver'])
CSRF=secrets.token_urlsafe(32)
@app.middleware('http')
async def protect(request:Request,call_next):
    if request.method=='POST' and request.headers.get('x-demo-token')!=CSRF:
        return Response('Missing browser session token',status_code=403)
    return await call_next(request)

app.mount('/static',StaticFiles(directory=str(ROOT/'static')),name='static')
@app.get('/')
def home(): return FileResponse(ROOT/'static/index.html')

@app.get('/api/bootstrap')
async def bootstrap():
    return {'token':CSRF,'as_of':FIXTURE['as_of'],'orders':await host.call('evidence','list_orders',{}),'outputs':outputs(),'trace':host.trace}

class PlanRequest(BaseModel):
    order_id:str=Field(max_length=40)
    condition:Literal['unused_with_packaging','opened_or_missing_parts']='unused_with_packaging'

@app.post('/api/plan')
async def plan(req:PlanRequest):
    try:
        ev=await host.call('evidence','get_evidence',{'order_id':req.order_id})
        busy=await host.call('calendar','get_busy_slots',{})
        result=make_plan(ev['order'],ev['policy'],busy,req.condition)
        return {**result,'trace':host.trace}
    except ValueError as e: raise HTTPException(400,str(e))

class ApprovalRequest(BaseModel):
    plan_id:str=Field(max_length=30)
    approved:bool=False
    fail_calendar:bool=False

@app.post('/api/approve')
async def approve(req:ApprovalRequest):
    if not req.approved: raise HTTPException(400,'Explicit approval required')
    try:
        p=load_plan(req.plan_id)
        token=issue_approval(p)
        result=await host.call('actions','prepare_approved_outputs',{'plan_id':req.plan_id,'approval_token':token,'fail_calendar':req.fail_calendar})
        return {'result':result,'outputs':outputs(),'trace':host.trace}
    except ValueError as e: raise HTTPException(400,str(e))

@app.get('/api/refund/{order_id}')
async def refund(order_id:str): return await host.call('evidence','get_refund_evidence',{'order_id':order_id})

@app.get('/api/audit')
def audit_log(): return {'audit':ledger(),'trace':host.trace}

@app.get('/api/download/{action_id}/{kind}')
def download(action_id:str,kind:str):
    action=next((a for a in outputs() if a['id']==action_id),None)
    if not action: raise HTTPException(404,'Output not found')
    if kind=='eml':
        m=EmailMessage();m['To']=action['email_draft']['to'];m['Subject']=action['email_draft']['subject'];m['X-Unsent']='1';m.set_content(action['email_draft']['body'])
        return Response(m.as_bytes(),media_type='message/rfc822',headers={'Content-Disposition':'attachment; filename=return-draft.eml'})
    if kind=='ics':
        from datetime import datetime,timezone
        def utc(s): return datetime.fromisoformat(s).astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        c=action['calendar']; text='\r\n'.join(['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//ReturnRelay//Demo//EN','BEGIN:VEVENT','UID:'+action_id+'@returnrelay.local','DTSTAMP:'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'),'DTSTART:'+utc(c['start']),'DTEND:'+utc(c['end']),'SUMMARY:'+c['title'],'BEGIN:VALARM','TRIGGER:-PT30M','ACTION:DISPLAY','DESCRIPTION:Prepare the return item and review merchant instructions','END:VALARM','END:VEVENT','END:VCALENDAR',''])
        return Response(text,media_type='text/calendar',headers={'Content-Disposition':'attachment; filename=return-reminder.ics'})
    raise HTTPException(404,'Unknown format')

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host='127.0.0.1',port=8000)
