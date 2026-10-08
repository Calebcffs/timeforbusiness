# R3 SERVO-CTO: attack on the top 10 clusters (vetoes on)

*2026-10-09. All hours and S$ are estimates unless linked. Rule applied: no code before a deposit or a signed pilot.*

## 1. "It's just a simple MVP": cluster by cluster

| # | Cluster | Software share | Build h | Upkeep h/wk (tech only) | Tool S$/mo | No-build test first | Severity |
|---|---|---|---|---|---|---|---|
| 1 | Corporate sports day | 5% | 5 (quote PDF) | 0 | 0 | Quote PDF to 5 founder-friend HR heads, 50% deposit | Minor tech; ops 10 to 14 h is the cost |
| 2 | Productized SME sites | 70%, but templated | 30 template + 10 per client | 3 to 5 at 10 sites (backups, edits, form PDPA) | 20 to 40 | Sell one site on Carrd/Wix + Calendly + Stripe link | Major: upkeep scales with clients |
| 3 | Youth camps | 15% | 6 | 1 | 0 to 25 | Google Form + PayNow link, pre-sell 8 spots | Minor tech; minors' data (PDPA) |
| 4 | Meet-day hub | 85% | 80 stated, 120 real | 3 to 5 in season, Saturday 7am support | 25 to 35 | Google Form entries, PayNow, Sheet, published results page | Major |
| 5 | Gear sourcing | 10% | 4 | 0 | 0 | Prepaid concierge post in a club WhatsApp chat | Minor tech |
| 6 | Adult/senior programmes | 5% | 4 | 0 | 0 | Clinic pilot, paper sign-up | Minor tech |
| 7 | Site-supply subscriptions | 10% | 6 | 1 | 0 to 15 | Invoice + Stripe subscription link | Minor tech; delivery is ops |
| 8 | Deposit kit/awards | 5% | 6 | 0 | 0 | Order form + deposit link | Minor tech |
| 9 | SME rule-change services | 10% (templates) | 0 | 0 | 0 | 3 accountants asked to refer | Major: liability, not tech |
| 10 | Own events series | 30% | 3 | 1 | 0 | Rent entry from a platform, not build | Minor tech |

**Finding:** 8 of 10 need a form, a payment link and a sheet, not software. Only 2 and 4 are real builds.

## 2. One reusable layer, not a platform

| Clusters | Shared need | Cheapest form |
|---|---|---|
| 3, 4, 6, 8, 10, baseline | Entries or sign-ups, payment, member record, confirmation, results or list page | One single-tenant template per organiser: Google Form + Sheet + PayNow/Stripe link + static Cloudflare Pages page. About 40 h once, 2 h/wk upkeep cap |

Multi-tenant SaaS stays vetoed (decided 2026-10-08). Cloudflare Pages static hosting is free ([costbench](https://costbench.com/software/cloud-infrastructure/cloudflare-pages-workers/free-plan/)). Stripe SG is 3.4% + S$0.50 on cards and 1.3% on PayNow ([worldfirst](https://www.worldfirst.com/sg/blog/international-transactions/stripe-fees-singapore/)).

## 3. Competitor check on the 3 most software-heavy

| Cluster | Finding (searched 2026-10-09) | Effect |
|---|---|---|
| 4 Meet hub | BEACON/SPARK "no incumbent" is **wrong**. HY-TEK Meet Manager is US$349 to 499 one-time ([HY-TEK](https://hytek.active.com/track-and-field-software.html)). Athletic.net AthleticLIVE is US$29 per meet ([Athletic.net](https://support.athletic.net/article/sxgcmdluz8-your-first-athletic-live-meet)). Race Roster runs road-race entry. Singapore Athletics still posts PDF results ([SA archive](https://archive.singaporeathletics.org.sg/category/singapore-open-track-field-championships/page/11/)). Whether SG school meets use HY-TEK is unverified | S$150 to 300 per meet must beat US$29. Wedge is local payment and school workflow only. Ceiling about S$2k |
| 2 Sites | Freelancer sites run SGD 1,500 to 8,000; basic packages SGD 2,000 to 5,000; small-site care plans SGD 50 to 350/mo ([launchd](https://launchd.it.com/guides/website-cost-singapore)). Wix/Squarespace S$14 to 49/mo | S$1,200 + S$59/mo is under market, so price is not the risk. Upkeep is |
| Booking/payment layer (3, 6, 10, baseline) | Spond free, payments USD 1 + 3.29% ([G2](https://www.g2.com/products/spond/pricing)); Calendly Teams about US$16 to 20/mo ([Cal.com](https://cal.com/blog/calendly-pricing)); Cal.com free tier | Off-the-shelf covers it. Custom is worth building only for athletics-specific fields |

## 4. Vetoes (build feasibility)

| Vetoed | Reason |
|---|---|
| Phone photo-finish timing and live results as a service (S1/cluster 4) | Accuracy on minors' results, Saturday-morning support, and 120 h before any meet director has said yes. Allowed: Sheets version |
| Garmin/Strava coach dashboard (V12) | API partner approval, 120 h |
| InvoiceNow micro-invoicing (V11) | Needs a Peppol access point; free incumbents |
| S4 condo tracker | Multi-tenant plus contractor passes sit beside the day job. Needs the Chairman's call |
| Any custom camp or kit-ordering app | Forms do it |

## 5. My TOP 5, each vs Club and Coach Desk

Baseline: about 6 h to launch, 7.3 h/wk steady, plateau S$2 to 3k, partner supply unproven.

| Rank | Pick | Build h / upkeep h/wk | Vs baseline |
|---|---|---|---|
| 1 | Cluster 1 corporate sports day | 5 / 0 tech | Beats: S$3 to 8k per event, no software, buyer holds a budget. Could not break it on tech; demand is the open question |
| 2 | Cluster 2 sites, **sold to two niches at once (clinics/studios and coaches)** | 30 / 3 | Beats: baseline is the coach-niche subset of this. A friend-led talk test runs both. Cap clients at 8 to stay under the 2 h/wk veto line |
| 3 | Cluster 3 youth camps | 6 / 1 | Beats: cash up front, no software. Fails on hours at 30 h peak, so cap at 2 camps a year |
| 4 | Cluster 8 deposit kit and awards | 6 / 0 | Ties on ceiling (S$2k), cheaper. A bridge that feeds clusters 1, 3, 4 |
| 5 | Cluster 4 meet hub, **Sheets version, free pilot only** | 8 / 1 | Door-opener, not a product. Worse than baseline on money, better on access to every club |

**Not broken, honestly:** I tried to break cluster 1's tech needs and couldn't, because a quote PDF, a Stripe link and a Sheet cover it. I did not test demand, which is not my lens. Blind-spot check: my top 5 is deliberately the least-code list. Nothing gets coded until 2 deposits.

Nothing is "just" anything. Who maintains it at 2am?
