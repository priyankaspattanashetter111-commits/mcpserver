# Prototype verification

Verified 24 November 2026 with Python 3.12 and official MCP SDK 1.29.0.

- 12 domain and safety tests passed.
- Integration passed: three actual MCP stdio services, initialization, tool discovery, evidence and calendar calls, approved output preparation, duplicate retry and refund-evidence distinction. Negotiated protocol: 2025-11-25.
- API checks passed: request token, preview, simulated failure with no partial outputs, approval, EML and ICS downloads, duplicate retry and replacement-only stop.
- Frontend JavaScript passed Node syntax validation.

Automated browser launch was blocked by the build environment. No claim of browser visual or end-user testing is made. Rehearse the browser flow manually on the recording machine. All providers use fictional local fixtures. Live API, cloud, model and production security validation are outside this prototype.
