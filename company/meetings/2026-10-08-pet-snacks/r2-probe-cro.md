# R2 PROBE-CRO: audit, K3 and talk test (vetoes ON)

*2026-10-08. "Source? Date? Sample size?" Sources checked today: AVS import page, HDB rules search, r1 files.*

## 1. Claim audit

| Claim (who) | Verdict | Why / source |
|---|---|---|
| Treats need "SFA registration plus TradeNet" (agenda, LEDGER #2, BEACON header) | **Contradicted** | AVS matter. Importer registration "not mandatory"; a CCP (S$22) is needed per consignment ([AVS](https://avs.nparks.gov.sg/businesses/commercial-importers-exporters/animal-feed/importing-pet-food), 2026-10-08; COGS [B][C]). Fix `04-setup-costs.md`. |
| Fish and insect are "non-meat" (SPARK #1/#5, COGS #3/#4, LEDGER #7/#8, BEACON #1) | **Unsupported** | AVS page does not define "meat" or mention fish or insect (2026-10-08). Chairman action: written AVS query. |
| Scheduled-country (AU/NZ/CA/UK/US) meat needs no source pre-approval, only a health certificate (COGS #5/#6) | **Supported** | Same AVS page. I tried to break it and couldn't. Dossier route is for non-scheduled origins only. |
| LEDGER #1 DTC S$13.90/50g, #4 S$15.90/50g, #10 S$20/pack | **Unsupported** | = S$27.8, S$31.8, S$40 per 100g. Highest observed shelf price is about S$27/100g (my r1). Every packs-per-month figure rests on these. |
| LEDGER China FD cost S$0.85-2/pack, 67% margin | **Unsupported** | Unvetted B2B listings. China is non-scheduled, so the dossier applies; LEDGER's "S$3k+" dossier cost has no source. |
| LEDGER retailer margin 45-60% | **Unsupported for SG** | US blog. LEDGER #6 resale at 23% already fails K6. |
| Pet Axis "only SG private-label producer", low MOQ (COGS, LEDGER #3) | **Unsupported** | Company claim via search. Price and MOQ unknown. |
| SPARK "cat treats 20.5% CAGR"; "94k cats" | **Blocked** | Same PetfoodIndustry article whose 1.3M cats I contradicted. |
| SPARK S$412M vs my Gitnux S$185M | **Blocked (both)** | Aggregator, different scopes, same site. Statista EUR132M is the best number (paywalled). |
| BEACON "85 clinics" | **Unsupported** | Cited to a cafe tag page. |
| BEACON 40-60% take samples, 10-20% stock; K-9 Artefacts "150+ shops" | **Unsupported / company claim** | BEACON admits unsourced. recordowl is a directory. |
| HDB: 2 cats and 1 approved dog; 62 breeds | **Supported (retail/media)** | Several 2026 guides; no HDB primary read. |

## 2. Version attack (up to 6)

| Version | Assumption | Sev. | Cheapest test |
|---|---|---|---|
| FD single-ingredient meat, AU/NZ (COGS #6) | Buyers pay above the S$27/100g ceiling vs 4+ local brands | Major | Two-price pre-order (section 5) |
| China FD chicken/fish (LEDGER #1) | Dossier is cheap and the plant will share documents | Major | Ask a distributor; no spend |
| Private label, SG maker (SPARK #7, LEDGER #3) | MOQ is light and brand owner needs no licence | Major | Written quote and AVS query |
| Fish/insect imports (COGS #3/#4) | AVS treats them as non-meat | Major (Fatal if wrong) | Written AVS query |
| Canicross/recovery (SPARK #9, LEDGER #10, BEACON #5) | A paying SG dog-runner pool exists | **Fatal as sole business** | Name an SG group and its size; BEACON found none |
| Groomer/cafe jar, curated resale (BEACON #3, COGS #1, LEDGER #6) | Sell-through and reorder; 23% margin clears K6 | Major | 10 walk-ins, consignment ask |

## 3. Demand stability (K3)

| Test | Result |
|---|---|
| Need over 5 years? | Ownership: yes (84k licensed dogs 2024 vs 70k in 2019; r1). Premium freeze-dried format: **unknown, no time series.** |
| Trap | Licensed cats 41k (Aug 2025) to 111k (Sep 2026) is **compulsory licensing catching up with existing cats**, not new demand. Dogs: 84k licensed vs 114k Euromonitor 2023 (search result, unverified). Do not read either as growth. |
| Driver | Structural for ownership and treats. Format may be a trend; Euromonitor flags price polarisation (squeeze in the middle). |
| Verdict | **Category passes K3. Specific versions below do not yet.** |

## 4. Vetoes and blocks

| Use | Target | Clears if |
|---|---|---|
| **K3 (narrow)** | Canicross/recovery as a business | A named SG running-dog group of 50+ members (estimate) or 10 owners prepay |
| **K3 (narrow)** | Insect treats | A local insect treat seller with a 12-month sales trail, or 3 of 10 owners pre-order |
| Block | All claims marked Unsupported/Blocked above | Source or "estimate" label |
| Block | "SFA registration" in setup costs | Corrected to AVS |
| Not used | Whole category, FD meat, private label | Ownership demand passes my tests |

## 5. My top 3, and versus Club and Coach Desk

1. **Curated resale of licensed SG-distributor SKUs** (zero licence). Weak margin (23%), fast demand probe.
2. **AU/NZ FD single-ingredient meat**: legal path is clear; price is the open question.
3. **SG private label**, if MOQ and licence quotes arrive light.

**No pet version beats CCD.** Hours 8-14 vs 7. LEDGER's own base case is S$2k by month 9-12 vs CCD S$2.5k. S$4k and S$6k need wholesale volume LEDGER rates unlikely. Pet snacks deserve at most a cheap test slot, not the lead.

## 6. Cheapest talk test (about 5 hrs, two weeks; estimates)

Clash: ideation-2 tests already use about 14 of the Chairman's hours; this fits only if run alongside the same contacts.

| Part | Action | Pass mark |
|---|---|---|
| A. Owners (10, from athletics contacts and friends who own dogs/cats) | Show one concept (single-ingredient FD, 50g). Half see S$12 (S$24/100g), half S$16 (S$32/100g). Ask for a refundable S$5 deposit by PayNow | 4 of 10 deposit, and at least 2 at S$16. Else price ceiling holds |
| B. Stockists (5 groomers/independent shops, walk-in) | Ask: "Would you stock this on consignment?" Ask category share and wholesale discount | 2 of 5 agree in writing or by message |
| C. Admin (no spend) | Written AVS query on fish, insect, brand-owner licence; one SG distributor quote | Answers in writing |

Pass A and B (03-criteria Stage C talk test plus one other) and the idea earns a landing-page test; fail either and drop it.
