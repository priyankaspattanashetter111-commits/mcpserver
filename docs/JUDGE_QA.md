# Judge questions and direct answers

## Why is MCP necessary

The business workflow can use direct APIs. MCP gives the host discoverable typed tools and replaceable services for evidence, calendar reads and controlled actions. We chose it to keep integrations modular and expose the approval boundary clearly. The prototype makes actual stdio MCP calls rather than labelling ordinary REST endpoints as MCP.

## What is different from a reminder app

Our proposed workflow ties each action to receipt evidence and a versioned policy, checks whether a refund return is appropriate, finds a preparation slot and prepares exact outputs after approval. Duplicate retries return the same local result. The differentiation is the combination and its demonstrable controls. We do not claim no other product has these features.

## Where is the AI

The delivered local host is deterministic. It proves the MCP and execution foundation first. A schema-constrained model adapter for forwarded-receipt extraction and plain-language explanations is the next feature. Eligibility, consent and execution checks remain outside that model. We should not claim an LLM already powers the current interface.

## Are you claiming INR 2,499 saved

No. That is the face value of a fictional receipt. A prepared request is not an accepted return or a refund. We only count recovered money after independent confirmation, which is not implemented here.

## What if the return is expired or replacement only

The workflow stops and explains the policy evidence. It does not invent an exception or initiate a refund request. The demo has separate fixtures for an expired window, replacement-only policy and unknown policy.

## What if the model follows malicious receipt instructions

The current host never interprets receipt prose as instructions. Future extraction will accept only a fixed schema and route uncertain results to review. An isolated action service will verify exact-plan approval, allowlisted effects and provider permissions. We must test adversarial documents before using any live model.

## What happens when one API succeeds and the next fails

The current demo creates local artifacts in one SQLite transaction, so either both local outputs commit or neither does. Real Gmail and Calendar cannot share that transaction. Our next build uses an outbox, provider IDs and reconciliation before retries, and offers compensation only when it is safe and explicitly approved.

## How do you know the deadline

In the demo, the fictional policy states the exact rule. In production, source policy text and merchant-local cutoffs must support the answer. Ambiguous rules stop for user or merchant confirmation.

## How will this work with real merchants

We start with draft preparation and a user handoff to the merchant's official workflow. We do not depend on a universal returns API or bypass merchant rules. Direct automated submission needs an authorized supported integration and separate approval.

## Can a model approve its own plan

There is no model in the delivered demo. Only the host's browser approval route can issue the signed authorization. The read services do not hold the signing key. This is a local architectural boundary. A future production system must authenticate the user and isolate the executor beyond processes sharing one local account.

## What can you finish in 24 hours

The narrow local workflow already runs. We would prioritize one consented receipt adapter, one Calendar integration, a durable outbox and tests. We would use forwarded receipts if OAuth setup delays access. Voice and broad merchant coverage are stretch goals.

## How will you validate demand and make money

Recruit an opt-in 30-person campus pilot, measure preparation time and completed eligible cases, and interview users who decline permission or abandon approval. Test a small free tier and INR 49 monthly plan. These are hypotheses. No paying users or validated market size are claimed.

## Are AWS and ElevenLabs already integrated

No. We show an optional AWS design for structured extraction and durable execution. Sponsor qualification requires checking the event rules and actually using the relevant services. Voice is a later optional interface, never a shortcut around written action review.

## What should the evaluator run

Install requirements, run `python host.py`, open localhost and select RR-1042. The README provides Windows and macOS/Linux commands. The tests cover local safety rules, actual MCP communication and the HTTP/download layer.
