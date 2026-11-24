# Submission checklist for 24 November 2026

Deadline: **24 November 2026, 11:59 PM IST**. The supplied portal screenshot says only the team leader can submit. The current CodeRIT FAQ additionally requires a GitHub repository. Follow later official announcements if they change these rules.

| Required item | What to provide | Final verification |
|---|---|---|
| PPT link | Official eight-slide template, no extra slides | Fill all team details, export as `SynError_Track1.pptx`, upload to Google Drive, set Anyone with the link can view |
| Video link | 3–5 minute YouTube video, public or unlisted | Open signed out, check audio, captions if possible, duration and completed upload processing |
| Repository link | GitHub project repository | Upload extracted source tree, README, diagrams and tests. Make it accessible to judges. Do not upload only the ZIP |
| Track | Track 1, Make MCP Matter | Match the PPT and submission form |
| Final submission | Team leader submits on Devnovate | Paste every URL, submit before cutoff, save the confirmation |

## Important timing difference

The supplied event overview refers to a 10-minute online pitch, while the submission checklist and current CodeRIT FAQ ask for a 3–5 minute uploaded video. Use the shorter script for today's submitted video. Use the 10-minute script for rehearsal or the later live online pitch if that timing is confirmed. Do not submit a 10-minute video unless organizers explicitly change the uploaded-video limit.

## Before exporting the deck

1. Open the presentation and replace college, team ID, member names and USNs. SynError comes from the supplied screenshot; correct it if needed.
2. Keep all eight template slides. Keep organizer logos and event information intact.
3. Confirm architecture labels distinguish the working local model from proposed cloud integrations.
4. Export/download as PowerPoint. Rename the file `SynError_Track1.pptx`.
5. Open the exported file once in PowerPoint or Google Slides and review diagrams and text wrapping.
6. Upload that file to Google Drive and test the viewer link in a signed-out/private browser.

## Upload the source to GitHub without command line

1. Sign in to GitHub and create a new repository, for example `returnrelay-mcp`.
2. Choose Public if appropriate for your team and the event. If private, explicitly grant the evaluator access according to organizer instructions.
3. Extract the provided prototype ZIP. Upload the files *inside* the `returnrelay` folder so `README.md` appears at repository root.
4. Include Python source, `requirements.txt`, `static`, `data/fixtures.json`, `tests`, `docs`, `.gitignore` and `Dockerfile`. Do not upload `.venv`, runtime databases, personal receipts or secrets.
5. Commit the files. Open the repository link signed out to verify access. A public repository is visible to everyone.

## Recording plan for a 4 minute 40 second video

- Record at 1080p with clear narration and a readable cursor.
- Show all eight slides in order. On slide 3, show the running demo briefly, then return to the slides.
- Focus on one eligible example, the approval gate and one blocked policy. Save lengthy setup and failure testing for questions.
- State that sample data is fictional and outputs remain local. Say that an AWS extension is proposed, not connected.
- Upload to YouTube as Unlisted or Public. Use a title such as `SynError | ReturnRelay | Track 1 | wHACKiest 2026`.
- Suggested description: `ReturnRelay connects purchase evidence and calendar availability through MCP to prepare a user-approved return draft and reminder. Local prototype with fictional sample data. Team SynError, Track 1, wHACKiest 2026. Repository: [paste actual repository URL].`
- Wait until upload processing completes, play the video, then paste its actual URL into Devnovate.

## Useful ready-to-paste project description

ReturnRelay is an MCP assistant for everyday purchase returns. It combines receipt evidence, versioned return policies and calendar availability to prepare a reviewable return request and reminder. An exact-plan approval gate and idempotent execution prevent silent or duplicate local actions. Expired, replacement-only and uncertain policies stop for human review. The working prototype includes three MCP services, an approval interface, downloadable draft and calendar files, and tests. Live provider adapters are the next build milestone.

## What this package does not do for you

It does not record or upload your spoken video, create a YouTube URL, upload the deck to your Google Drive, publish a GitHub repository, or submit the form. Those steps need your team account and final review. No placeholder URL should be submitted as a real link.

Source checked 24 November 2026: https://whackiest-2026.vercel.app/ FAQ 6–13 and uploaded event screenshots. The wording in the portal may change, so check for a later announcement before the final submit action.
