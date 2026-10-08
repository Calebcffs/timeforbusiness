# R1 SERVO-CTO: build-leverage ideas

*Lens: what Caleb can vibecode or assemble with no-code in under 40 hrs, run in under 2 hrs/week, and sell to a Singapore business. Default to off-the-shelf until someone pays.*

## Part 1: Fresh ideas (idea cards)

| # | Name | Buyer | Offer + revenue | Channel partners | Startup (est.) | Build h / upkeep h per wk | Why demand lasts | Biggest risk |
|---|---|---|---|---|---|---|---|---|
| A | **WhatsApp front desk** for tuition, dance, music and enrichment centres | Centre owner / admin | S$900 setup + S$150/mo retainer; client pays own platform fee. FAQ, trial-class booking, renewal chasers | Tuition/enrichment associations, centre-software vendors, landlords of studio malls | S$500 (est.) | 25 / 1.5 (up to 5 clients) | Parents live on WhatsApp; admin staff cost rises | Platform margin and churn; Meta now bills service replies too (see sources) |
| B | **60-second lead responder** for aircon, cleaning, renovation firms | Owner-operator | S$600 setup + S$120/mo. Replies to ad/Carousell/web leads, collects photos, books a quote slot | Google Ads freelancers, supplier/wholesaler reps, trade associations | S$300 (est.) | 15 / 1 | Lead-chasing is a daily pain; whoever replies first wins | Owners ignore the tool after 2 months |
| C | **CoachKit**: site + booking + Stripe in a box | Independent coach / small studio | S$490 setup + S$49/mo hosting and edits | Coaching bodies, gyms, sports shops | S$300 (est.) | 12 / 1 | Coaches keep starting out; new ones need a presence | Local rival Vibefam from S$89/mo, Acuity from US$16. Wedge is price and "done for you" only |
| D | **PDPA/DNC starter pack** (AI-drafted policy, consent forms, breach checklist) | SME owner with no DPO | S$199 one-off + S$99/yr update. Not legal advice; positioned as templates | Corp secretaries, accountants, bookkeepers (referral fee) | S$200 (est.) | 15 / 0.5 | Law is permanent; outsourced DPOs run S$100 to S$500/mo, so the cheap tier is open | Liability if a client is fined. Needs disclaimer and a lawyer's read |
| E | **Gift quote engine**: web form to auto-quote hampers by headcount, budget, date; supplier ships | HR / admin buyer | S$30 to S$80 per box at roughly 30% margin (est.), plus repeat annual orders | Event planners, HR consultancies, dried-food suppliers | S$3k to S$8k (est.) | 20 / 3, lumpy | Corporate gifting recurs every year | Seasonal; supplier reliability. Tech removes admin, not stock risk |
| F | **Name-engraved awards** for clubs and schools, outsourced to a local engraver at first | Club secretary / teacher | S$15 to S$40 per piece; ordering page with live preview | Sports clubs, school CCAs, trophy shops | S$500 to S$1k (est.) | 15 / 3 | Annual awards cycle | Outsourced margin may be thin; own laser means HDB and ventilation issues |
| G | **Coach progress reports**: Claude turns session notes into client reports and plans | Personal trainer / running or swim coach | S$59 to S$99/mo per coach | Gyms, coach associations | S$200 (est.) | 20 / 1 | Coaches sell on visible results | Willingness to pay. Trainerize-style apps exist |

**CTO ranking by buildability:** B, A, C, G, D, F, E.

**Tool costs for LEDGER (cited, currency unconfirmed):** Wati from about 119/mo, SleekFlow Pro AI about 149/mo, Respond.io from 79/mo. Meta Singapore rates: utility and service about S$0.02 per message, marketing about S$0.09. [Sleekflow pricing](https://sleekflow.io/en-sg/blog/whatsapp-business-price), checked 2026-10-08. Studio software: [Vibefam](https://vibefam.com/why-fitness-studios-are-transitioning-from-mindbody-and-glofox-to-local-solutions/), checked 2026-10-08. DPO prices: [SG Secretary Services](https://www.singaporesecretaryservices.com/singapore-pdpa-compliance-for-smes-costs-and-fees-breakdown/), checked 2026-10-08.

**Veto note:** I veto building our own WhatsApp stack on the Meta API. Resell or configure a no-code platform. Also avoid clinics for A: patient data raises PDPA exposure, and clinics already have booking systems.

**Watch, not a card:** PSG pays up to 50% of pre-approved solutions but merges into EDGE in H2 2026, so the vendor-approval path is unclear ([Sleekflow PSG guide](https://sleekflow.io/en-sg/blog/psg-grant-singapore)). InvoiceNow setup is free from vendors until 2031, so no paid wedge.

## Part 2: Verdicts on the old list (`02-ideas.md`)

| Old # | Verdict | Reason |
|---|---|---|
| 1 Coach website + booking | **Merge into C/G** | Right buyer, thin wedge. Add the AI report layer to differentiate |
| 5 WhatsApp/AI for clinics and tuition | **Keep, narrow into A and B** | Drop clinics (PDPA health data) |
| 6 Corporate gifting | **Keep, merge with E** | Tech quote engine is the edge |
| 2 Dried foods, 25 Pantry staples | **Merge into E** | Dried food becomes a gift SKU, not a store |
| 11 Uniforms/merch | **Merge into F** | Same school/club buyer |
| 14 Home-services leads | **Merge into B** | Sell the responder tool, not disputed leads |
| 4 Website builder app, 13 Directory, 15 Event platform | **Cut** | Saturated or slow, and AI makes building cheap for everyone |
| 12 Local SEO, 16 Templates, 21 VA agency | **Cut** | Crowded or time-for-money |
| 3 Pet food, 7 Eldercare | **Cut from my lens** | No tech edge, heavy regulation. COGSWORTH to judge |

Nothing is "just" anything. Who maintains it at 2am? Every digital card above stays at 1 to 1.5 hrs/week only because the platform is rented, not built.
