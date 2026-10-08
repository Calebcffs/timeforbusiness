# R2 COGSWORTH-COO: cross-challenge (2026-10-08)

*Hours are my **estimates** from per-task assumptions: admin 1 h/wk; outreach 3 h/wk; onboarding a WhatsApp client 6 h one-off; support 1.5 h/month per light client, 2 to 2.5 for client data. Legal facts were checked today and sources are linked. Where I could not confirm a point, it is labelled.*

## 1. Weekly hours vs the 10-hr cap

| Idea (merged) | Launch (wks 1-8) | Steady state | Verdict |
|---|---|---|---|
| **Centre Desk** (SERVO A + LEDGER L3 + my #5): build 4, outreach 4, onboarding 2, admin 1 | 11 | 10 clients: 8.9. 13 clients: 9.9 | Fits. **Cap about 12-13 light clients** |
| **Recall engine**, vets and groomers (PROBE D + L2 vertical) | 11 | 8 clients: 9.6 | Tight |
| Same engine for GPs, dentists or maid agencies (2.5 h/mo each, plus DPA paperwork) | 11 | 8 clients: 10.6 | Breach |
| **CoachKit**: outreach 3, 2 setups/mo at 5 h, support 1.5, admin 0.5 | 6 | 7.3 | Fits; the problem is willingness to pay, not hours |
| **Hamper**, self-packed: sourcing 3, outreach 5, admin 2.5, pack and deliver 4, billing 1 | **15.5** for 8 wks, three windows a year | Yearly average about 7.5 | **"That's 15 hours a week. You have 10."** Outsourced packing and delivery: 9.5 |
| **Dementia kit**: B2B plus B2C, 30 orders/mo | 9 | 8.1; 9.3 at 40 orders | Fits, but caregiver messages are uncapped |
| **PDPA-Pack**, white-label | 7 (15 h one-off build) | 4 | Fits |

**B2B capacity:** one person supports about **12 to 13** light WhatsApp or booking clients in 10 hrs/week. That falls to **8** for clients with sensitive data, and rises to about 17 if partners feed leads so outreach drops to 1 h. At S$129/mo that is **S$1.7k MRR**, which is LEDGER's base case. The cap equals the plan, so growth must come from price (S$250+), not client count.

## 2. Licences and compliance: a form, a fee, or a wall

| Item | Class | Detail | Source |
|---|---|---|---|
| DPO appointment | Form, free | Required of every organisation | [PDPC DPO](https://www.pdpc.gov.sg/dpo) |
| Data intermediary role (we hold clients' patient, student or maid data) | Contract and process | We carry the protection and retention duties. A breach must be reported to the client "without undue delay" | [PDPC DI guide](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/Guide-to-Managing-Data-Intermediaries--2020.pdf) |
| Health data | Higher care, **not a ban** | PDPA has no separate "sensitive" tier, but PDPC expects stronger protection and consent for health information. WhatsApp use is allowed with consent | [PDPC healthcare guidelines](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/advisory-guidelines-for-the-healthcare-sector-sep-2023.pdf) |
| NRIC and FIN numbers | **Do not collect** | General prohibition. This hits maid-agency and clinic recall | [PDPC NRIC guidelines](https://www.pdpc.gov.sg/guidelines-and-consultation/2020/02/advisory-guidelines-on-the-personal-data-protection-act-for-nric-and-other-national-identification-numbers) |
| DNC | Client's duty | Applies to B2C marketing messages, not B2B. Whether appointment reminders count is **unconfirmed** | [PDPC DNC](https://www.pdpc.gov.sg/overview-of-pdpa/do-not-call-registry) (not fetched) |
| HSA device (dementia kit) | **Depends on product** | HSA says devices have a physical or mechanical effect on the body and diagnose, alleviate or treat a condition. General-wellness items are out. Manufacturers, importers and wholesalers need a licence, and Class A is exempt only from product registration | [HSA](https://www.hsa.gov.sg/announcements/how-medical-devices-are-regulated-by-hsa/) |
| Electrical items | Form | Controlled goods need CPS registration | [CPS](https://www.consumerproductsafety.gov.sg/suppliers/cpsr/overview-of-cpsr/) |
| Hamper repacking | **Wall** if you repack | Unlicensed repacking was fined S$2,500. Buying sealed packs: **unconfirmed**, so ask SFA | [SFA](https://www.stg.sfa.gov.sg/news-publications/newsroom/2024/sunrise-food-pte-ltd-fined--2-500-for-operating-a-non-retail-food-business-without-a-licence) |

**(a) Dementia kit, ruling.** I over-blocked in R1 (my blind spot). PROBE is right: a **non-electronic, non-monitoring kit** (labelled storage, large-print calendar clocks, photo albums, contrast tableware) with **no treatment claims** sits on the wellness side of HSA's own line. It needs no licence. Three things push a kit into device territory: body-worn sensors or GPS trackers, any "reduces agitation" claim, and medication dispensers. HSA has not confirmed whether wander door-alarms count, and I could not find a ruling. I still hold the wall for monitors: a wholesaler licence needs GDPMDS or ISO 13485, from my R1 source, which I should re-verify. **K4 is not used**; the cut becomes "kit, yes; monitors, no".

**(b) WhatsApp products.** Each is paperwork, not a blocker: consent wording, a DPA with each client, no NRIC or FIN, and a data-retention rule. Hours are already counted above.

## 3. Attack table

| Idea | Assumption | Severity | Cheapest test |
|---|---|---|---|
| Centre Desk | "1.5 h/wk for 5 clients" (SERVO). Onboarding and Meta template approval are my 6 h one-off per client | Major | Onboard one free pilot and time-log it |
| Recall engine | Health-adjacent clients tolerate S$99-199/mo; vets lack reminders | Major (PROBE's own flag) | Ask 3 vet practices what they use now |
| CoachKit | Coaches pay S$40-99/mo against free tools | Major | Talk test of 5 NROC coaches |
| Hamper (BEACON 8 peak, LEDGER 6) | Both undercount peak. I count 15.5 | Major | Written quote from a licensed packer; need 30% margin or more after fees |
| Dementia kit | The 5 SKUs are non-device | Major, not Fatal | Run the SKU list through HSA's classification tool |
| PDPA-Pack | Cosecs will not build their own; we avoid selling legal advice | Major | Ask 3 cosecs or accountants if they would white-label |

I tried to break **Centre Desk** on licences and couldn't, because it needs none beyond the PDPA paperwork above. I tried to break **CoachKit** on hours and couldn't, because it totals 7.3.

**Concessions.** My #2 (direct-import dried food) dies: 7 hrs for a 15-25% margin and S$530 profit. My hamper hours (15 peak) were right, and the fix is outsourced packing. I defend my R1 cuts of medical-device resale only.

## 4. Merges

1. **Centre Desk + Recall + Helper-Cycle = one WhatsApp engine**, verticals tested in order: tuition and studios, then vets and groomers. Clinics and agencies last.
2. **PDPA-Pack folds into the engine** as the consent-and-DPA template bundle we ship with it. That removes the liability of a standalone product.
3. **Hampers + gift quote engine + Agent-Gift Desk = one preorder-only idea** with outsourced packing.

## 5. TOP 5 and kills

1. **Centre Desk**: no licence, 9 hrs, recurring.
2. **Vet and groomer recall**: same engine, new vertical, 9.6 hrs.
3. **CoachKit**: 7 hrs, no licence, the Chairman's seed; WTP is untested.
4. **Dementia kit, non-device only**: strongest demand, fits hours, needs the HSA check first.
5. **Preorder hamper, packing outsourced**: time-boxed; deposits must start now for CNY.

**Kill:** Helper-Cycle (FIN data, small slow-paying agencies). Monthly dried-food drop (S$530 profit, a TradeNet permit every shipment). Gift quote engine (a 20 h build to dodge no problem). Supplier emissions pack (8 hrs of consulting). Grant-ready tool (fails K5 until EDGE rules are published).

## 6. Vetoes

**K2:** not used. Hamper self-packed breaches at 15.5, so I attach a condition (outsource) instead. **K4:** not used.
