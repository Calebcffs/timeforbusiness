# ROD Inc. Operating Protocol

## Why files

The robots are Claude Code subagents. They can't talk to each other directly, and each one starts with no memory. So **all debate lives in files**, and the main Claude session (the "facilitator") runs each robot in turn and passes along what the others wrote.

## Shared state

| File | Purpose | Who writes |
|---|---|---|
| `company/meetings/YYYY-MM-DD-<topic>.md` | One file per meeting, every round appended in order | Each robot, its own section only |
| `company/assumptions.md` | Every load-bearing assumption, its owner, challenger, status and evidence | Any robot adds; PROBE-CRO updates status |
| `company/decisions.md` | Dated log of what the Chairman ratified or vetoed | RIVET-CEO drafts, Chairman approves |
| `research/<idea>.md` | Evidence files per idea | PROBE-CRO mainly |

## Meeting format (one round by default)

1. **Agenda.** The Chairman or facilitator states the question, e.g. "Which 5 ideas go to deep research?" The facilitator creates the meeting file and picks a **proposer** plus **2 challengers**, chosen from the attack-target table in [ROSTER.md](ROSTER.md).
2. **Proposal.** The proposer writes a memo: claim, reasoning, path to profit (price x volume minus cost, months to breakeven), and the load-bearing assumptions.
3. **Challenge.** Each challenger attacks in writing:
   - Name each assumption they think is wrong or untested.
   - Give a severity: **Fatal**, **Major** or **Minor**.
   - Propose the cheapest test that would settle it.
   - Agreeing is allowed only as "I tried to break X and couldn't, because <evidence>". Disagreeing just to disagree is not allowed.
4. **Rebuttal.** The proposer concedes, defends with evidence, or revises.
5. **Vetoes.** Any robot with a relevant veto (see ROSTER) states whether they use it, and why.
6. **Synthesis.** RIVET-CEO writes the recommendation, keeps dissent visible ("LEDGER-CFO still objects because…"), and lists next actions.
7. **Chairman.** You ratify, veto or send it back. The result is logged in `decisions.md`.

8. **Report (every meeting, from 2026-10-09).** The facilitator produces a PDF board report for every meeting:
   1. Write `executive-summary.md` in the meeting folder (as RIVET-CEO, plain English, no veto codes). It starts with a one-paragraph answer as a `>` blockquote, then: what to do now, the shortlist in plain English, how it compares with the baseline, what was dropped and why, the next two weeks, decisions needed from the Chairman, how to read the rest, and what changed since the last report.
   2. Write `report.json` in the meeting folder (reference `ROD-BR-<year>-<nnn>`, title, question, date, contributors, decision ID, round titles). Copy one from an earlier meeting.
   3. Run `python company/tools/build_report.py company/meetings/<meeting-folder>`. The PDF lands in `company/reports/`.
   4. Look at a few rendered pages before telling the Chairman it is done.

A second round runs only if the Chairman asks for one or a Fatal challenge is still unresolved.

## Ideation meetings (added 2026-10-09)

Ideation runs in two phases so early ideas are not killed before they are written down.

| Phase | Vetoes | What happens |
|---|---|---|
| 1. Diverge | **Suspended for everyone.** No robot may kill or reject an idea. | Each robot lists many ideas from an assigned source (not just its job lens). SPARK-CIO clusters and dedupes. |
| 2. Converge | **Back on.** | The core robots attack the top ideas, vetoes apply, RIVET-CEO synthesizes. |

Other changes for ideation:
- Ideas are tested against the **income ladder** in `01-constraints.md` (S$2k, S$4k, S$6k a month), because the Chairman has not set a single income target.
- The founder's strengths and the **day-job industry exclusion** in `01-constraints.md` apply to every idea.
- Parallel runs are allowed for a whole round once the Chairman has approved the run count.

## Rules of engagement

1. **Profit is the tiebreaker.** Every argument must connect to money in or money out.
2. **Attack the assumption, not the robot.**
3. **Numbers need a source and date, or the label "estimate".** PROBE-CRO can block unlabeled numbers.
4. **Stay inside the Chairman's constraints.** No robot may propose breaking [01-constraints.md](../01-constraints.md). Only the Chairman can change it.
5. **No external actions.** Robots never contact people, spend money, sign up for services or push to git. They write files. The facilitator handles git after the Chairman approves.
6. **Keep sections short.** About 300 words per robot per round. Tables over prose.
7. **Address the Chairman as "the Chairman" or "Caleb", using they/them.**

## Cost control

- Each robot run is a fresh agent that rereads the files, so a meeting costs roughly 1 run per participant.
- A default meeting is **4 runs**: proposer, 2 challengers, then CEO synthesis. A rebuttal adds 1.
- A full 6-robot round is about 7 runs. Ask the Chairman before running one.
- Robots run **one at a time** by default, which also prevents edit collisions in the meeting file. Run in parallel only with Chairman approval.
- Optional: set `model: sonnet` in a robot's file for cheaper, lower-stakes roles.

## Running a meeting

Ask the facilitator: **"Run a ROD board meeting on <topic>"**. The facilitator states the planned participants and run count, then waits for your go-ahead.
