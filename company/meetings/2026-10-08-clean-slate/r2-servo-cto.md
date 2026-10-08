## SERVO-CTO: Challenge (Round 2)

*Nothing is "just" anything. Who maintains it at 2am? Hours and upkeep are estimates unless sourced. WhatsApp facts checked 2026-10-08.*

### WhatsApp reality check (conflict a)

| Rule | Fact | Consequence |
|---|---|---|
| Business verification | Meta: typically 1 to 3 business days; 3 to 5 days end-to-end via a BSP ([Hyperleap](https://hyperleap.ai/whatsapp-business-api/how-to-get)) | Delay is the client's documents and Facebook Business Manager access, 2 to 3 hrs chasing per client (est.) |
| Templates | Review minutes to 24 hrs ([Meta docs](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-review/)). Appointment reminders are Utility; "come back and rebook" nudges are Marketing | Recall wording decides the price tier and approval risk |
| Cost per message (SG) | Utility S$0.016, marketing S$0.0732; service replies chargeable from 1 Oct 2026 ([Sleekflow](https://sleekflow.io/blog/whatsapp-business-price)). Another source shows S$0.0205 and S$0.0937 before GST ([ChatMaxima](https://chatmaxima.com/whatsapp-api-pricing/singapore/)). Discrepancy unresolved | 400 messages a month is under S$30 per client. Meta fees are not the cost. |
| Platform seat | Wati, Respond.io and Sleekflow run about 79 to 149/mo (R1, currency unconfirmed) | A S$150 retainer plus a client-paid seat makes S$250+ a month. Too dear for solo tutors. |
| Limits and consent | 250 contacts per 24 hrs until verified, 1,000 after. Opt-in is required. DNC and PDPA consent for marketing messages: verify with PDPC | Fine at this scale. Consent logging is a build task. |

**Can the Chairman run it on a rented no-code platform?** Yes, for up to about 5 to 10 clients, if each client owns its own WhatsApp Business account and the Chairman only configures it. No, if the Chairman hosts the Meta API or builds a multi-tenant app.

### Attack table (top ideas from any robot)

| Idea | Assumption | Sev | Cheapest test (no build) |
|---|---|---|---|
| Recall engine (SERVO A, CFO L3, COO 5, PROBE D) | The client's customer list and dates are clean and digital. They are usually in a notebook or a vendor's system. I tried to break "owners will pay S$150/mo" and could not, but I have no evidence it holds. | Major | Chairman sends reminders by hand from the free WhatsApp Business app for 1 pilot client for 4 weeks. Count rebookings. |
| Clinic recall (CFO L2, PROBE E) | Clinics will let an outsider near patient data | Fatal | None. Park it until a non-clinical vertical pays. |
| CoachKit (all five robots) | Coaches pay S$40 to 49/mo against free Linktree and a rival from S$89/mo | Major | A one-page landing page with a Stripe payment link, sent to 10 coaches on the registry. Count deposits. |
| Hamper preorder (CFO L4, BEACON Agent-Gift, COO 1) | Buyers commit before the CNY window closes. Ordering is 10 to 12 weeks ahead (CFO), so the window is now. | Major | A quote PDF sent to 10 HR contacts. Take a 50% deposit before buying stock. |
| PDPA-Pack (my D, BEACON PDPA-Pack) | AI-drafted templates are safe to sell as a product | Fatal | I concede. It needs a lawyer's read (est. S$500 to 1,500) and carries fine liability. Ask 3 cosecs whether they would resell it before anything else. |
| Lead responder (my B) | Owners reply through a tool, not their own WhatsApp number | Major | Chairman answers leads by hand for 2 firms for 2 weeks with a script. |

### Build hours vs the 10 hrs/week cap

| Idea | Build (h) | Per-client onboarding (h) | Upkeep at 5 clients (h/wk) | Sales (h/wk) | Fits cap? |
|---|---|---|---|---|---|
| Recall engine, one vertical | 25 (sheet, 4 templates, consent text, DPO form) | 5 | 2 (4 at 10 clients) | 3 to 4 | Yes to about 10 clients. My R1 figure of 1.5h was too low once support is counted. |
| CoachKit | 8 (template site) | 5 | 1 (3 at 15) | 3 | Yes, but edit requests grow with every client |
| Hamper | 4 (quote sheet) | n/a | 3 average, 15 for 6 weeks | 3 | Peak breaches K2 unless packing is outsourced |
| Lead responder | 15 | 4 | 1 | 3 | Yes. Retention is the problem. |

### Merges

| Merge | Result | One platform? |
|---|---|---|
| Recall engine = SERVO A + CFO L2/L3 + PROBE D/E + COO 5 + BEACON Helper-Cycle | Core is the same: a contact sheet, a date field, a template and an opt-in log. Only the wording and consent text change between tuition, groomers, maid agencies and coaches' pack renewals. | Reuse one set of templates and sheets. Do not build multi-tenant software. Pick ONE vertical by talk test. Maid agencies add helper medical data and FINs, so they come last. |
| Hampers = CFO L4 + BEACON Agent-Gift + COO 1 + SERVO E | One preorder project | Zero build. Drop my quote engine. |
| Merch = CFO L6 + COO 6 + SERVO F | One drop-ship offer | Zero build |

### TOP 5 (any robot's)

1. **Recall engine, one vertical**, tuition or pet groomers. It is the only recurring revenue that shares one core.
2. **Hamper preorder**, sealed packs only. Zero build and time-critical. I could not break the idea, but peak hours are the risk.
3. **CoachKit as the entry offer**, with recall as the upsell. Cheapest test, thinnest wedge.
4. **Merch and awards drop-ship.** Zero build, with an annual cycle.
5. **Dementia home kit (PROBE B).** The strongest structural driver on the board, and it needs no build from me. Condition: non-medical items only, and a memory-clinic talk test first.

**Kill:** my PDPA/DNC pack (liability), my coach progress reports and gift quote engine (building before demand), standalone Helper-Cycle (health data, tiny agencies), InvoiceNow setup (free from IRAS and vendors, as I noted in R1), clinic recall for now.

**Veto:** used narrowly. I veto a self-hosted Meta API stack and any multi-tenant SaaS. No idea is vetoed outright. Clinic recall is blocked on data risk, not on build skill.
