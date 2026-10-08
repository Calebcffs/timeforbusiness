## PROBE-CRO: Challenge (Round 2)

*Checked 2026-10-08. "Unsupported" = no source found, not proven false.*

### Claim audit

| Claim | Robot | Verdict | Source + date |
|---|---|---|---|
| ConnectLah and Bot MD serve SG clinics | BEACON | Bot MD: Supported (NEMG case). ConnectLah: Unsupported as "already serves". Listing says "launched 5mo ago", 0 reviews, no client count | [Product Hunt](https://www.producthunt.com/products/connectlah); [Bot MD](https://botmd.io/en/blog/nemg-clinics-adopt-an-omnichannel-approach-to-patient-appointment-scheduling-through-bot-md) |
| Clinic recall is an open gap (L2, my E) | LEDGER, PROBE | **Contradicted** (I concede E). Free HAS "Queue" SMS tool, MOH-approved gov.sg SMS for Healthier SG outreach, plus the two above | [ask.gov.sg](https://ask.gov.sg/has/questions/cmh4hrc9i014bf9d6ggifranj) |
| Tuition WhatsApp is a gap | SERVO, LEDGER, COGSWORTH | Partly contradicted. SchoolTracs from S$55/mo/branch, Edulabs S$300/mo, ClassRec free tier, Schooli does attendance via WhatsApp. Gap only for an inbound-enquiry and trial-booking front desk: no source shows any vendor offers it | [SchoolTracs, 23 Jul 2026](https://www.schooltracs.com/sg/blog/best-tutoring-software-singapore-compared/) (vendor-written, biased) |
| Eldercare "HSA risk" (cut by LEDGER, BEACON, COGSWORTH) | all three | **Overstated.** HSA regulates by intended use: monitoring body functions is a device, general-wellbeing items are not. Wholesaler licence applies to devices only | [HSA](https://www.hsa.gov.sg/announcements/how-medical-devices-are-regulated-by-hsa/) |
| SMF subsidises listed devices only | BEACON | Supported, and means-tested (income cap S$2,000 per person) | [AIC/HealthHub](https://healthhub.sg/a-z/costs-and-financing/seniors-mobility-and-enabling-fund-smf) |
| Eldercare inventory "S$10k+" | LEDGER | Unsupported, no source or SKU list | none |
| Meta bills service replies from 1 Oct 2026; 1,000 free/month | SERVO, LEDGER | Supported | [Sleekflow, 2026-10-08](https://sleekflow.io/blog/whatsapp-business-price) |
| WA rates: utility S$0.016 vs ~S$0.02; marketing S$0.0732 vs S$0.09 | LEDGER vs SERVO | Conflict, currency unconfirmed (Meta bills in USD). Immaterial (under S$10/mo) | same |
| Hamper unit price: S$20-60 (BEACON), S$40-150 (COGSWORTH), S$150-250 (LEDGER) | three | Contradicted among themselves. Hamper margin 30-40% is unsourced; about 468 SG firms in the gifts-wholesale SSIC code | [Straits Data](https://straitsdata.com/companies/sg/q-e-hampers/53292599L) |
| 6,100 coaches on NROC | BEACON | Supported | [SportSG](https://www.sportsingapore.gov.sg/support-resources/national-registry-of-coaches/) |
| 6-monthly helper medical is mandatory | BEACON | Supported | [MOM](https://www.mom.gov.sg/passes-and-permits/work-permit-for-foreign-domestic-worker/eligibility-and-requirements/six-monthly-medical-examination) |
| Dementia 74k to 152k | PROBE | Supported (MOH, 4 Nov 2025). Projection, not a count | [MOH](https://www.moh.gov.sg/newsroom/number-of-dementia-afflicted-patients-over-five-year-period-and-future-projections-for-singapore/) |
| 718 MOE tuition centres | LEDGER | Unsupported and stale (2022) | none |
| Any willingness-to-pay or conversion rate (5-15% intro-to-sale; S$40-150/mo prices) | BEACON, SERVO, LEDGER, mine | Unsupported. All are estimates | none |

### Attack on the promising ideas

| Idea | Assumption | Severity | Cheapest test |
|---|---|---|---|
| Dementia kit (mine) | Caregivers pay S$80-250 for non-device kits when Dementia Singapore has its own retail store and caregivers get cash grants (HCG up to S$600/mo from Apr 2026, means-tested) | Major | Call 5 day-care centres and memory clinics. Preorder 10 units of one SKU |
| Tuition/enrichment front desk | Centres pay S$150/mo on top of a S$55 system | Major | 5 talk tests: do they lose enquiries on WhatsApp today? |
| PDPA pack | SMEs buy S$199 templates; liability stays low | Major | Ask 3 cosecs if they would refer, and what they charge now (DPO S$100-500/mo, [SG Secretary Services](https://www.singaporesecretaryservices.com/singapore-pdpa-compliance-for-smes-costs-and-fees-breakdown/)) |
| CoachKit | Coaches pay S$40-99/mo vs Vibefam from S$89 | Major | Show a mock site to 5 NROC coaches |
| Helper-Cycle | Agencies pay S$150/mo and share helper data under PDPA | Major | 3 agency calls |
| CNY hampers (L4) | 80 boxes sold by 10-12 week lead time | **Fatal if no buyers by mid-Nov** | Ask 10 HR contacts for a deposit before any stock |

### Merges

- Coach site (G), CoachKit, L1, COGSWORTH 3 and SERVO G are one idea.
- PDPA-Pack and SERVO D are one idea.
- Tuition (C, SERVO A, L3, COGSWORTH 5) is one idea. Clinics (E, L2) are dropped.
- Hampers, dried food, pantry and merch (BEACON 4, SERVO E and F, L4 to L6, COGSWORTH 1, 2 and 6) are one idea family.

### Top 5 (my ranking)

1. **Dementia non-device kit**, narrowed. Structural driver, no regulatory wall. I concede the evidence is thin on willingness to pay.
2. **Tuition and enrichment front desk**, bundled with admin.
3. **PDPA starter pack** via cosecs. A permanent legal duty and sourced competitor prices.
4. **CoachKit**, merged. The reachable list exists (6,100).
5. **Helper-Cycle**, as a reserve.

**Kill:** clinic recall (E, L2) is contradicted by free government tools. InvoiceNow (A) is contradicted by IRAS's free service, so I withdraw it. F is time-for-money. L5 and the pantry ideas fail on margin.

I tried to break COGSWORTH's "repacking needs a licence" and couldn't, because SFA fined a dried-food supplier S$2,500 in 2024.

**Demand stability:** the dementia, tuition, PDPA and 6ME drivers are structural. Coaching willingness to pay is unproven. Hampers are structural but lumpy and crowded.

**Veto / evidence blocks:** K3 not used. Evidence block: the unsourced willingness-to-pay figures and the hamper margin and price figures should not be treated as fact until they are sourced or labelled "estimate". Source? Date? Sample size?
