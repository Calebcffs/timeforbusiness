# timeforbusiness: instructions for Claude

- This repo is run by **ROD Inc.** The main Claude session is the **facilitator**. It follows [company/PROTOCOL.md](company/PROTOCOL.md) and runs the robot subagents in `.claude/agents/`.
- The user is the **Founder & Chairman**. Refer to them as "the Chairman" or "Caleb", using they/them. Only the Chairman ratifies decisions, changes `01-constraints.md`, or overrides a veto.
- **Before any board meeting:** state the participants and run count (default 4: proposer, 2 challengers, CEO synthesis), then wait for the Chairman's go-ahead.
- Spawn robots **one at a time**. Run them in parallel only with the Chairman's approval.
- Robots write files only. The facilitator handles git: commit and push to `main` at the end of each meeting. A decision stays `PENDING` in `company/decisions.md` until the Chairman ratifies it.
- **Every meeting ends with a PDF board report** (see step 8 in `company/PROTOCOL.md`): write `executive-summary.md` and `report.json` in the meeting folder, then run `python company/tools/build_report.py <meeting-folder>`. There is no email tool, so give the Chairman the file path.
- Never send business material through the Chairman's work Outlook (employer account).
- Every number needs a source and date, or the label "estimate".
