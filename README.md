# timeforbusiness

A systematic way to decide **what business to start** in Singapore, and what it costs to set up.

End goal: a thriving, durable business. Not a specific product. The product is chosen by the process below.

## The company: ROD Inc.

Planning is run by **ROD Inc. (Robots of Doom Incorporated)**. That's 6 robot executives (Claude Code subagents in `.claude/agents/`) plus the human Chairman. They debate in files and attack each other's assumptions, and the Chairman decides.

- [company/ROSTER.md](company/ROSTER.md): who's who, attributes, vetoes, attack targets
- [company/PROTOCOL.md](company/PROTOCOL.md): how a board meeting runs, and cost control
- [company/assumptions.md](company/assumptions.md): assumption register
- [company/decisions.md](company/decisions.md): decision log

To run a meeting, open Claude Code in this repo and say "Run a ROD board meeting on <topic>".

## Funnel

| Stage | File | Question it answers | Status |
|---|---|---|---|
| 1 | [01-constraints.md](01-constraints.md) | What can I actually afford, and what am I good at? | done (v1) |
| 2 | [02-ideas.md](02-ideas.md) | What are all the candidate ideas? | v1 (30 ideas, unresearched) |
| 3 | [03-criteria.md](03-criteria.md) | How do I kill and score ideas fairly? | done (v1) |
| 4 | [04-setup-costs.md](04-setup-costs.md) | What does any SG business cost to legally start? | v1 (sourced) |
| 5 | `research/<idea>.md` | Unit economics + demand evidence for each finalist | not started |
| 6 | `DECISION.md` | The pick, plus a 30-day validation plan | not started |

## Rules of the process

1. **Kill cheap, research expensive.** Most ideas die at the kill filter in minutes. Only survivors get deep research.
2. **Evidence beats vibes.** Every number in `research/` has a source link and a date. Market data goes stale, so each file records when it was checked.
3. **Validate before buying.** No inventory or build spend until a cheap demand test passes (landing page, preorder, 5 partner conversations).
4. **One idea researched at a time.**

## Next action

Review the shortlist in [02-ideas.md](02-ideas.md), cut or add ideas, then pick which 5 go to deep research.
