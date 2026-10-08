# R1 SERVO-CTO: vibecoding and website ideas (diverge, no vetoes)

*Source: vibecoding and website knowledge at 20 hrs/week. All numbers are estimates unless linked. Tool costs checked 2026-10-08.*

**Tool cost anchors:** Cloudflare Pages free tier, unlimited static bandwidth ([costbench](https://costbench.com/software/cloud-infrastructure/cloudflare-pages-workers/free-plan/)); Supabase Pro US$25/mo ([jetadmin](https://www.jetadmin.io/blog/supabase-pricing-2026-guide-to-plans-limits-and-real-world-costs/)); Stripe SG card 3.4% + S$0.50, PayNow 1.3% ([aspire](https://aspireapp.com/en-sg/blog/stripe-payment-processing-singapore-businesses)). Competitors on club software: Spond free (payments 3.29% + $1), Sportlyzer from EUR24/mo, Glofox from US$99/mo ([capterra SG list](https://www.capterra.com.sg/alternatives/144279/sportlyzer), [G2 Spond](https://www.g2.com/products/spond/pricing)).

| # | Idea (build hrs) | Buyer | How they pay | Channel partner | Startup S$ | Hrs/wk | S$2k / 4k / 6k | Founder fit | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Coach Site Kit**: productized site + booking + PayNow for solo coaches/small clubs, any sport, athletics first (40h) | Head coach / club secretary | S$900 setup + S$39/mo | Athletics clubs, SA | 500 | 10 | Y / maybe / N | Athletics network, websites | Baseline family; Spond/Glofox gap for lightweight SG tools |
| 2 | **MeetDesk**: entries, heats, start lists, results pages for small meets (80h) | Meet organiser (club, school) | S$150 to 300 per meet | Clubs, school sports heads | 500 | 8 | maybe / N / N | Athletics network | Own insight; meet run on Excel (estimate) |
| 3 | **DSA Athlete Portfolio**: structured athlete profile page + PDF for Secondary 1 sports DSA (30h) | Parent of student athlete | S$99 one-off, S$29/yr update | Coaches who recommend it | 300 | 5 | maybe / N / N | Athletics parents, coaches | [MOE DSA-Sec portal opens May](https://woodlandssec.moe.edu.sg/dsa/) |
| 4 | **Kids academy waitlist and make-up class manager** (60h) | Owner of kids' enrichment studio | S$49/mo | Friends who own studios | 800 | 6 | Y / maybe / N | Friends, business sense | Pain mining on parent chat groups (estimate) |
| 5 | **SG Athletics results and PB database**, free pages, paid athlete/coach tier (70h) | Athlete, parent, coach | S$5/mo or S$40/yr; sponsors | SA, clubs | 500 | 6 | N / N / N | Athletics network | Results scattered across PDFs (estimate) |
| 6 | **SG sports events calendar + newsletter** (race, meet, tournament), paid listings (25h) | Event organiser, sports brand | S$50 to 150 per listing, sponsors | Organisers | 300 | 5 | maybe / N / N | Athletics network | Races listed across [Endorphins](https://endorphinsrunning.com/races/byd-singapore) and others |
| 7 | **Clinic/tuition site + WhatsApp booking pack** (non-construction), 7-day delivery (30h per client template, 10h per client) | Clinic, tuition centre, groomer owner | S$1,200 + S$59/mo | Friends' referrals | 600 | 12 | Y / Y / maybe | Websites, friends | Productized-agency model |
| 8 | **Coach plan storefront**: coaches sell training plans as PDFs/subscriptions, ROD takes 15% (50h) | Coach | 15% of sales | Athletics coaches | 800 | 5 | N / N / N | Athletics network | Creator-storefront analogy |
| 9 | **PDPA-in-a-box for SMEs**: notice generator, DPO checklist, annual refresh (30h) | Small business owner | S$199/yr | Accountants, friends | 400 | 4 | N / N / N | Business knowledge | [PDPC free generator exists](https://www.3ecpa.com.sg/resources/tools/singapores-data-protection-notice-generator/) |
| 10 | **ActiveSG slot-release alerts** via Telegram (35h) | Badminton/tennis player | S$3 to 5/mo | Sports groups | 200 | 3 | N / N / N | Vibecoding | [Slot scarcity, scripts policed](https://www.sportsingapore.gov.sg/media-centre/booking-of-activesg-facilities/) |
| 11 | **STRETCH: InvoiceNow-ready micro-invoicing** for tiny GST firms (150h+, Peppol access point needed) | Micro-SME owner | S$15/mo | Accountants | 3,000 | 8 | maybe / maybe / N | Business knowledge | [IRAS mandate phases to 2031](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/gst-invoicenow-requirement) |
| 12 | **STRETCH: Garmin/Strava coach dashboard**, team training load view (120h, API partner approval) | Coach / club | S$5 per athlete/mo | Athletics coaches | 1,000 | 6 | maybe / N / N | Athletics, sports tech | Coaches juggle app screenshots (estimate) |

## Top 3 I want tested

**#7** because it is the only idea here that plausibly hits S$4k: 5 clients a month at S$1,200 plus a recurring base, with friends as the channel, and it is the least sports-dependent. **#1** because it is the baseline family and a talk test costs nothing; testing it next to #7 shows whether the athletics niche beats a general local-business niche. **#3** because DSA is a fixed annual date with parents already spending on coaching; it is cheap to build and a coach referral would show instantly whether the channel works. Note my blind spot: all three should get a talk test and a pre-sale before I write code, and a no-code first version (Carrd, Calendly, Stripe links) is enough.

## Tags vs round 1

| # | Tag | Round 1 link |
|---|---|---|
| 1 Coach Site Kit | OVERLAP | Club and Coach Desk (shortlist #2); angle: any sport, productized |
| 2 MeetDesk | NEW | none |
| 3 DSA Athlete Portfolio | NEW | none |
| 4 Kids academy waitlist | OVERLAP | Centre Desk (#1), different job (waitlist/make-up, not enquiry) |
| 5 Results/PB database | NEW | none |
| 6 Events calendar | OVERLAP | killed "directory / event platform" cluster |
| 7 Clinic/tuition site + WhatsApp | OVERLAP | Centre Desk and the killed clinic recall; angle: site-led, one-off fee |
| 8 Coach plan storefront | NEW | merch add-on in #2 is different |
| 9 PDPA-in-a-box | OVERLAP | R1 PDPA pack (previously cut) |
| 10 ActiveSG alerts | NEW | none |
| 11 InvoiceNow micro-invoicing | OVERLAP | killed InvoiceNow |
| 12 Garmin coach dashboard | NEW | nearest is killed "coach reports" |

Tally: 6 NEW, 6 OVERLAP. Nothing here is rejected; overlaps with Round 1 kills (#6, #9, #11) are listed so SPARK can cluster them.
