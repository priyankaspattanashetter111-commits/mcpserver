# ReturnRelay narration scripts

Use the 3–5 minute version for the submitted YouTube video. The longer version is for rehearsal or a confirmed ten-minute live pitch.

## Ten minute presentation

### Slide 1: Team introduction

0:00 to 0:40

Hello judges. We are team SynError, and our Track One proposal is ReturnRelay. We are addressing an ordinary task that becomes surprisingly fragmented: returning an online purchase before its deadline. ReturnRelay brings the receipt, the policy and the user's availability into one reviewable plan. We have prepared a working local prototype with real MCP services. Our focus is useful assistance with clear evidence and explicit control over every action.

Presenter cue: Speak calmly. Replace the team placeholders before recording. Do not read USNs aloud.

### Slide 2: Problem Statement

0:40 to 1:50

Consider a student who buys headphones for two thousand four hundred and ninety-nine rupees. The product is unsuitable, and the student wants to return it. The receipt is in email, the return policy is somewhere else, and their calendar is full. They still need to check whether a refund return is allowed, find time to prepare the item, contact the merchant and later follow the refund. A missed step can leave the task unfinished. This example is illustrative. We are not presenting the receipt value as money already saved. A reminder can tell the user a date, while a merchant portal can handle that merchant's process. The coordination still falls on the buyer. Our initial audience is frequent online shoppers among students and early-career professionals. We propose a thirty-person campus pilot to test whether this specific coordination problem is frequent and painful enough to justify a product.

Presenter cue: Keep the example concrete. The pilot is planned, not completed.

### Slide 3: Proposed Solution

1:50 to 3:20

ReturnRelay prepares a return request and a calendar reminder using an evidence-linked plan. The user selects a purchase and declares the item's condition. The host reads the receipt and versioned policy through one MCP service, then reads availability through another. Rules check the policy and deadline. If the policy is unclear, replacement only, or expired, the workflow stops and explains why. For an eligible case, the user sees the source evidence, the exact email recipient and text, and the proposed reminder time. Only after approval does the action service prepare the two local outputs. Let me show the preview for our sample headphones. The amount is the receipt value, and the displayed time is for preparing the return, not a booked pickup. The current MVP uses fictional data. It creates downloadable draft and calendar files, and it does not send messages, submit returns or issue refunds.

Presenter cue: Allow about 18 seconds inside this segment to open the running app, select RR-1042 and click Preview. Show the evidence and approval checkbox. Return to slide 4.

### Slide 4: Tech Stack

3:20 to 4:25

We chose a small stack so the core workflow stays understandable and buildable. The interface uses HTML, CSS and JavaScript with no frontend build step. A Python FastAPI host manages the request and applies deterministic rules. The official Python MCP SDK runs three separate services over standard input and output. These are actual protocol connections with initialization, tool discovery and tool calls. SQLite stores the exact plan, prepared outputs and local audit records. The current host does not use an LLM. Our next AI feature is constrained extraction of fields from a user-forwarded receipt, followed by validation against source evidence. An optional AWS design uses Bedrock for extraction and cloud storage and execution services later. Those services are proposed. We are not claiming an AWS deployment or sponsor integration already works.

Presenter cue: Explain MCP as a standard interface between the host and services. Avoid describing every dependency version aloud.

### Slide 5: Process Flow and Architecture

4:25 to 6:15

The architecture has a deliberate boundary between reading information and preparing actions. The browser asks the FastAPI host for a plan. The host calls the evidence MCP service for a receipt and policy, and the calendar MCP service for occupied times. The planner calculates the cutoff and searches for a free thirty-minute preparation slot. In our fixed demonstration, the policy says delivery date plus seven calendar days, ending at eleven fifty-nine PM in India. That makes the sample deadline November twenty-sixth. The planner skips the occupied five-to-six PM class and suggests six PM. It then saves and displays the complete plan. When the user approves, the host signs a short-lived authorization tied to the exact stored content. The action MCP service checks the signature, expiry and current policy before preparing outputs. A unique plan identifier prevents duplicates on retry. In this local model, the draft and reminder commit together in one SQLite transaction. Real email and calendar services need a durable outbox, provider identifiers and reconciliation because they cannot share this transaction. Finally, a merchant notice saying processed remains separate from verified bank credit.

Presenter cue: Reserve about 15 seconds to show approval and retry in the app. Say that one local output pair exists. Do not say the calendar file is already imported or that money was refunded.

### Slide 6: Novelty and Innovation

6:15 to 7:35

Our proposed differentiation is the evidence-linked action plan. A manual reminder depends on the user to supply the deadline and perform the steps. A merchant portal provides that store's process. ReturnRelay coordinates the evidence and the user's availability through replaceable MCP tools, then asks for approval of the exact effects. The plan binds the receipt, policy version, recipient, message and reminder time together. If that content changes, the old authorization is no longer valid. Retry protection prevents a repeated click from creating another local output pair. This comparison describes approaches, not a complete audit of competing products. We are not claiming that no other product offers similar features. MCP also deserves a precise explanation: direct APIs could implement this workflow. We use MCP for typed tool discovery and replaceable services, with a clear boundary between reading evidence and taking an approved action. That combination gives judges something specific to inspect and test.

Presenter cue: Emphasize the working control mechanism. Avoid words such as world's first, guaranteed or fully autonomous.

### Slide 7: Impact and Feasibility

7:35 to 9:00

The first feasibility evidence is the working local implementation. Twelve domain tests passed, covering the cutoff, occupied time, unsupported policies, missing approval, changed plans, expiry, duplicate retries and failure recovery. Separate integration checks exercised real MCP communication and the HTTP download workflow. We still need a manual browser rehearsal before recording. For the next twenty-four-hour build, we would prioritize a receipt adapter, one calendar connection, the approval boundary and a durable outbox. If OAuth setup delays live access, user-forwarded receipts preserve the core demonstration. We would add model extraction only behind strict validation. For impact, our proposed pilot target is preparation below two minutes, with zero unauthorized actions. Those are targets, not measured results. We will compare manual and assisted completion for the same task and record corrections, abandoned plans and duplicate effects. The local demo needs no paid model API. Real hosting, model and support costs must be measured before scaling. Our scope deliberately avoids automatic merchant submissions until a supported integration exists.

Presenter cue: If asked about automated browser testing, explain that the build environment blocked browser launch. Domain, protocol and API checks ran successfully.

### Slide 8: Business Model and Closing

9:00 to 10:00

We would begin with an opt-in campus pilot of thirty people, recruited from a proposed outreach pool of one thousand contacts. Our pricing hypothesis is a free allowance of three active purchases and a forty-nine-rupee monthly plan. At one hundred paying users that would be four thousand nine hundred rupees in monthly gross revenue, before costs and tax. We have not validated conversion or willingness to pay. We would reach initial users through campus communities and referrals, and measure repeated use before expanding. We do not propose selling receipt data. ReturnRelay's value is a completed, reviewable preparation workflow backed by evidence, with the user controlling the next action. Thank you. We are ready to demonstrate both the successful path and the cases where the assistant stops.

Presenter cue: Finish at ten minutes. For the submitted YouTube link, use the shorter script that follows.

## Submission video storyboard

### Slide 1: Introduction

0:00 to 0:20

Hello judges. We are team SynError. Our Track One project is ReturnRelay, an MCP assistant that prepares a reviewable return request and reminder from purchase evidence and calendar availability. We have a working local prototype.

### Slide 2: Problem

0:20 to 0:55

A buyer who wants to return a product must find the receipt, interpret the policy, find time before the deadline and contact the merchant. Those steps span apps. A reminder gives a date, while the buyer still coordinates the task. Our example uses a fictional two-thousand-four-hundred-and-ninety-nine-rupee purchase. We propose testing the problem with thirty campus users.

### Slide 3: Solution and brief demonstration

0:55 to 1:45

ReturnRelay reads purchase and policy evidence through MCP, checks eligibility and suggests a free preparation slot. The user reviews the exact email and reminder before approving. Here is our sample plan. The sources and effects are visible before approval. Expired, replacement-only and unclear policies stop for review. This local demo prepares files. It does not send email, book a pickup or refund money.

Presenter cue: Use about 15 seconds to show the running app preview. Return to slide 4.

### Slide 4: Stack

1:45 to 2:15

The interface uses plain web technologies. FastAPI hosts deterministic planning. Three services use the official Python MCP SDK over stdio, and SQLite stores plans and outputs. The current host has no LLM. A proposed AWS Bedrock adapter would extract receipt fields with validation. Live provider and cloud integrations remain next milestones.

### Slide 5: Architecture

2:15 to 3:10

The host reads receipt evidence and occupied calendar time through separate MCP services. It displays the complete plan. Explicit user approval lets the host sign authorization for that exact content. The action service verifies authorization, expiry and policy before creating outputs. A unique plan identifier makes retries return the existing pair. Both local files commit together. Real external APIs need an outbox and reconciliation. Merchant processing evidence never becomes an automatic claim of bank credit.

Presenter cue: Spend about 10 seconds pointing across the architecture. If the app is ready, show one approved output and the duplicate-free retry result.

### Slide 6: Differentiation

3:10 to 3:45

Our differentiation is the combination of source evidence, exact action review and reliable local execution. The same plan binds policy, recipient, draft and slot. MCP provides discoverable tools and replaceable services. Direct APIs could implement the workflow too. We make a specific, testable design claim rather than claiming a global first.

### Slide 7: Feasibility

3:45 to 4:20

Twelve domain tests passed, plus real MCP and API checks. The next build prioritizes one receipt adapter, calendar integration and a durable outbox. Forwarded receipts provide a fallback if OAuth setup delays access. The pilot target is preparation below two minutes with zero unauthorized actions. These outcomes still need measurement.

### Slide 8: Business and closing

4:20 to 4:40

We propose a thirty-user opt-in pilot, then test a small free tier and forty-nine rupees per month. Pricing and demand remain hypotheses. ReturnRelay helps users prepare a return with evidence and control. Thank you.
