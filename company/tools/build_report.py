"""Build the ROD Inc. board report PDF for one meeting.

Usage:  python company/tools/build_report.py company/meetings/<meeting-folder>

Reads  <meeting-folder>/report.json   (metadata, round titles)
       <meeting-folder>/executive-summary.md   (written by RIVET-CEO, plain English)
       <meeting-folder>/{synthesis,agenda,r1-*,r2-*,...}.md
       company/assumptions.md, company/decisions.md
Writes company/reports/<ref>_<slug>.pdf (path printed at the end).
Needs:  pip install reportlab   (and Arial/Consolas TTFs from C:\\Windows\\Fonts).
"""
import json, re, sys
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
                                Table, TableStyle, KeepTogether, NextPageTemplate, HRFlowable,
                                ListFlowable, ListItem)
from reportlab.platypus.tableofcontents import TableOfContents

MEET = Path(sys.argv[1]).resolve()
REPO = MEET.parents[2]
CFG = json.loads((MEET / "report.json").read_text(encoding="utf-8"))
OUTDIR = REPO / "company" / "reports"
OUTDIR.mkdir(exist_ok=True)
OUT = OUTDIR / f"{CFG['ref']}_{CFG['slug']}.pdf"

F = r"C:\Windows\Fonts"
for name, fn in [("Arial", "arial.ttf"), ("Arial-Bold", "arialbd.ttf"), ("Arial-Italic", "ariali.ttf"),
                 ("Arial-BoldItalic", "arialbi.ttf"), ("Consolas", "consola.ttf")]:
    pdfmetrics.registerFont(TTFont(name, f"{F}\\{fn}"))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic", boldItalic="Arial-BoldItalic")

NAVY, ORANGE, GREY = colors.HexColor("#14213D"), colors.HexColor("#E4572E"), colors.HexColor("#5B6475")
LIGHT, RULE = colors.HexColor("#F2F4F8"), colors.HexColor("#C9CFDA")
CALLOUT = colors.HexColor("#FFF3EC")


def S(name, **kw):
    base = dict(fontName="Arial", fontSize=9.2, leading=13, textColor=colors.HexColor("#1E2430"))
    base.update(kw)
    return ParagraphStyle(name, **base)


st = {
    "body": S("body", spaceAfter=5), "bullet": S("bullet", spaceAfter=2),
    "cell": S("cell", fontSize=7.4, leading=9.4),
    "cellh": S("cellh", fontSize=7.4, leading=9.4, fontName="Arial-Bold", textColor=colors.white),
    "H1": S("H1", fontName="Arial-Bold", fontSize=18, leading=22, textColor=NAVY, spaceAfter=8),
    "H2": S("H2", keepWithNext=1, fontName="Arial-Bold", fontSize=12.5, leading=16, textColor=NAVY, spaceBefore=10, spaceAfter=5),
    "H3": S("H3", keepWithNext=1, fontName="Arial-Bold", fontSize=10.5, leading=14, textColor=ORANGE, spaceBefore=8, spaceAfter=4),
    "H4": S("H4", keepWithNext=1, fontName="Arial-Bold", fontSize=9.4, leading=13, textColor=NAVY, spaceBefore=6, spaceAfter=3),
    "note": S("note", fontName="Arial-Italic", fontSize=8.4, leading=11.5, textColor=GREY, spaceAfter=6),
    "toc1": S("toc1", fontName="Arial-Bold", fontSize=10, leading=15, textColor=NAVY),
    "toc2": S("toc2", fontSize=9, leading=13, leftIndent=14, textColor=GREY),
}


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(t):
    t = esc(t)
    t = re.sub(r"`([^`]+)`", r'<font face="Consolas" size="8">\1</font>', t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" color="#1B5FBF"><u>\1</u></a>', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r"\1", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\*\w])\*(?!\s)([^*]+?)(?<!\s)\*(?![\*\w])", r"<i>\1</i>", t)
    return t


def make_table(rows, width):
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    weights, mins = [], []
    for c in range(ncol):
        m = max(len(re.sub(r"[*`]", "", r[c])) for r in rows)
        lw = max((len(w) for r in rows for w in re.sub(r"[*`]", "", r[c]).split()), default=4)
        weights.append(max(min(m, 60), 5))
        mins.append(min(max(lw * 4.0 + 9, 20), 70))
    extra = width - sum(mins)
    cw = [width * mn / sum(mins) for mn in mins] if extra < 0 else [mn + extra * w / sum(weights) for mn, w in zip(mins, weights)]
    data = [[Paragraph(inline(c.strip()), st["cellh"] if i == 0 else st["cell"]) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=cw, repeatRows=1)
    style = [("BACKGROUND", (0, 0), (-1, 0), NAVY), ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("GRID", (0, 0), (-1, -1), 0.4, RULE), ("LEFTPADDING", (0, 0), (-1, -1), 3.5),
             ("RIGHTPADDING", (0, 0), (-1, -1), 3.5), ("TOPPADDING", (0, 0), (-1, -1), 2.5),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]
    style += [("BACKGROUND", (0, i), (-1, i), LIGHT) for i in range(2, len(rows), 2)]
    t.setStyle(TableStyle(style))
    return t


def md_to_flowables(text, width, demote=1):
    out, lines, i, para, bullets, numbered = [], text.splitlines(), 0, [], [], False

    def flush_para():
        nonlocal para
        if para:
            out.append(Paragraph(inline(" ".join(para)), st["body"])); para = []

    def flush_bullets():
        nonlocal bullets, numbered
        if bullets:
            items = [ListItem(Paragraph(inline(b), st["bullet"]), leftIndent=16) for b in bullets]
            if numbered:
                out.append(ListFlowable(items, bulletType="1", leftIndent=16, bulletFontName="Arial", bulletFontSize=9))
            else:
                out.append(ListFlowable(items, bulletType="bullet", start="•", leftIndent=14, bulletFontName="Arial", bulletFontSize=8))
            out.append(Spacer(1, 4)); bullets = []; numbered = False

    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            flush_para(); flush_bullets()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i]):
                    rows.append([c.replace("\\|", "|") for c in re.split(r"(?<!\\)\|", lines[i].strip().strip("|"))])
                i += 1
            out += [make_table(rows, width), Spacer(1, 7)]
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            flush_para(); flush_bullets()
            out.append(Paragraph(inline(m.group(2)), st[f"H{min(len(m.group(1)) + demote, 4)}"]))
        elif re.match(r"^\s*[-*]\s+", ln):
            flush_para(); bullets.append(re.sub(r"^\s*[-*]\s+", "", ln))
        elif re.match(r"^\s*\d+\.\s+", ln):
            flush_para(); numbered = True; bullets.append(re.sub(r"^\s*\d+\.\s+", "", ln))
        elif ln.strip() == "---":
            flush_para(); flush_bullets()
            out.append(HRFlowable(width="100%", thickness=0.5, color=RULE, spaceBefore=4, spaceAfter=4))
        elif ln.strip() == "":
            flush_para(); flush_bullets()
        else:
            flush_bullets()
            s = ln.strip()
            if s.startswith("*") and s.endswith("*") and not s.startswith("**") and not para:
                out.append(Paragraph(inline(s), st["note"]))
            else:
                para.append(s)
        i += 1
    flush_para(); flush_bullets()
    return out


def callout(text, width):
    """Shaded box used for 'the answer' in the executive summary."""
    t = Table([[Paragraph(inline(text), S("co", fontSize=10, leading=14.5))]], colWidths=[width])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), CALLOUT), ("LINEBEFORE", (0, 0), (0, -1), 3, ORANGE),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return t


class Doc(BaseDocTemplate):
    def afterFlowable(self, fl):
        if isinstance(fl, Paragraph) and fl.style.name in ("H1", "H2tocable"):
            key = f"h{id(fl)}"
            self.canv.bookmarkPage(key)
            self.notify("TOCEntry", (0 if fl.style.name == "H1" else 1, fl.getPlainText(), self.page, key))


W, H = A4
LM = 18 * mm
CW = W - 2 * LM
REF = CFG["ref"]


def on_page(canv, doc):
    canv.saveState()
    canv.setStrokeColor(RULE); canv.setLineWidth(0.5)
    canv.line(LM, H - 14 * mm, W - LM, H - 14 * mm)
    canv.setFont("Arial", 7.5); canv.setFillColor(GREY)
    canv.drawString(LM, H - 11.5 * mm, f"ROBOTS OF DOOM INCORPORATED  |  Board Report {REF}")
    canv.drawRightString(W - LM, H - 11.5 * mm, "CONFIDENTIAL")
    canv.line(LM, 13 * mm, W - LM, 13 * mm)
    canv.drawString(LM, 8.5 * mm, CFG.get("footer", "Estimates are labelled as such. This is a test list, not a launch list."))
    canv.drawRightString(W - LM, 8.5 * mm, f"Page {doc.page}")
    canv.restoreState()


def on_cover(canv, doc):
    canv.saveState()
    canv.setFillColor(NAVY); canv.rect(0, 0, W, H, stroke=0, fill=1)
    canv.setFillColor(ORANGE); canv.rect(0, H * 0.40, W, 5 * mm, stroke=0, fill=1)
    canv.restoreState()


doc = Doc(str(OUT), pagesize=A4, leftMargin=LM, rightMargin=LM, topMargin=20 * mm, bottomMargin=19 * mm,
          title=f"ROD Inc. Board Report: {CFG['title']}", author="RIVET-CEO, Robots of Doom Incorporated",
          subject=f"Board Report {REF}")
doc.addPageTemplates([PageTemplate(id="cover", frames=[Frame(LM, 20 * mm, CW, H - 40 * mm, id="c")], onPage=on_cover),
                      PageTemplate(id="main", frames=[Frame(LM, 19 * mm, CW, H - 39 * mm, id="m")], onPage=on_page)])
story = []
cov = lambda n, **k: ParagraphStyle(n, fontName=k.pop("fontName", "Arial"), **k)

# ---- cover
story += [Spacer(1, 38 * mm),
          Paragraph("ROBOTS OF DOOM INCORPORATED", cov("c1", fontName="Arial-Bold", fontSize=13, leading=18, textColor=ORANGE)),
          Paragraph("(ROD Inc.)", cov("c1b", fontSize=10, leading=14, textColor=colors.HexColor("#AEB6C8"))),
          Spacer(1, 14 * mm),
          Paragraph("Board Report", cov("c2", fontName="Arial-Bold", fontSize=34, leading=40, textColor=colors.white)),
          Paragraph(CFG["title"], cov("c3", fontSize=20, leading=26, textColor=colors.white)),
          Spacer(1, 10 * mm),
          Paragraph(CFG["question"], cov("c4", fontName="Arial-Italic", fontSize=12, leading=17, textColor=colors.HexColor("#AEB6C8"))),
          Spacer(1, 52 * mm)]
meta = [["Reference", REF], ["Date", CFG["date"]], ["Prepared for", "Caleb, Founder and Chairman"],
        ["Prepared by", "RIVET-CEO, Chief Executive Officer"], ["Contributors", CFG["contributors"]],
        ["Status", f"For Chairman ratification (decision {CFG['decision_id']} is pending)"], ["Classification", "Confidential"]]
ct = Table([[Paragraph(a, cov("m1", fontName="Arial-Bold", fontSize=8.5, leading=12, textColor=colors.HexColor("#AEB6C8"))),
             Paragraph(b, cov("m2", fontSize=9.5, leading=12, textColor=colors.white))] for a, b in meta],
           colWidths=[34 * mm, CW - 34 * mm])
ct.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                        ("TOPPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
story += [ct, NextPageTemplate("main"), PageBreak()]

story.append(Paragraph("Contents", st["H2"]))
toc = TableOfContents(); toc.levelStyles = [st["toc1"], st["toc2"]]
story += [toc, PageBreak()]

n = 0


def H1(t):
    global n
    n += 1
    story.append(Paragraph(f"{n}. {t}", st["H1"]))


def H2t(t):
    story.append(Paragraph(t, ParagraphStyle("H2tocable", parent=st["H2"])))


def read(fn):
    return re.sub(r"^# .*\n", "", (MEET / fn).read_text(encoding="utf-8"), count=1)


# ---- executive summary: optional first block "THE ANSWER: ..." is rendered as a callout
H1("Executive summary")
es = (MEET / "executive-summary.md").read_text(encoding="utf-8")
m = re.match(r"^\s*>\s*(.+?)\n\n", es, re.S)
if m:  # leading blockquote = the one-paragraph answer
    story += [callout(" ".join(l.lstrip("> ").strip() for l in m.group(1).splitlines()), CW), Spacer(1, 8)]
    es = es[m.end():]
story += md_to_flowables(es, CW, demote=1)
story.append(PageBreak())


def part(title, files, intro=None):
    H1(title)
    if intro:
        story.append(Paragraph(inline(intro), st["note"]))
    for label, fn in files:
        if label:
            H2t(label)
        story.extend(md_to_flowables(read(fn), CW, demote=1))
    story.append(PageBreak())


LAB = {"spark-cio": "SPARK-CIO", "probe-cro": "PROBE-CRO", "beacon-cmo": "BEACON-CMO", "servo-cto": "SERVO-CTO",
       "ledger-cfo": "LEDGER-CFO", "cogsworth-coo": "COGSWORTH-COO", "rivet-ceo": "RIVET-CEO"}
LAB.update(CFG.get("labels", {}))
ORDER = ["spark-cio", "probe-cro", "beacon-cmo", "servo-cto", "ledger-cfo", "cogsworth-coo", "rivet-ceo"]

part("Synthesis", [("RIVET-CEO: full synthesis", "synthesis.md")], "Written by RIVET-CEO after reading every round file. Reproduced in full.")
part("Meeting agenda", [("Agenda as issued", "agenda.md")])
for prefix, (title, intro) in sorted(CFG["rounds"].items()):
    files = sorted((p for p in MEET.glob(f"{prefix}-*.md")),
                   key=lambda p: (ORDER.index(p.stem[len(prefix) + 1:]) if p.stem[len(prefix) + 1:] in ORDER else -1, p.name))
    part(title, [(LAB.get(p.stem[len(prefix) + 1:], p.stem[len(prefix) + 1:]), p.name) for p in files], intro)

H1("Assumptions register and decision log")
for label, f in [("Assumptions register", "assumptions.md"), ("Decision log", "decisions.md")]:
    H2t(label)
    story.extend(md_to_flowables(re.sub(r"^# .*\n", "", (REPO / "company" / f).read_text(encoding="utf-8"), count=1), CW, demote=1))
story.append(PageBreak())

H1("Sign-off")
board = [["Robot", "Title", "Vetoes held"],
         ["LEDGER-CFO", "Chief Financial Officer", "K1 capital, K6 margin, K7 time to profit"],
         ["SERVO-CTO", "Chief Technology Officer and engineer", "Build feasibility"],
         ["COGSWORTH-COO", "Chief Operating Officer (operations and compliance)", "K2 weekly hours, K4 legality"],
         ["PROBE-CRO", "Chief Research Officer", "K3 demand stability; evidence block"],
         ["BEACON-CMO", "Chief Marketing Officer (growth and partnerships)", "K5 path to customers"],
         ["SPARK-CIO", "Chief Ideas Officer", "None, ever"],
         ["RIVET-CEO", "Chief Executive Officer", "None (tie-breaker only)"]]
sign = [Paragraph(CFG.get("signoff_note", "This report records the full discussion of the ROD Inc. board, including dissent. "
                          "Nothing in it has been acted on. No one outside the company has been contacted, and no money has been spent. "
                          "Every number is an estimate unless a source is shown in the underlying section."), st["body"]),
        Spacer(1, 10), Paragraph("Respectfully submitted,", st["body"]), Spacer(1, 16),
        Paragraph("RIVET-CEO", ParagraphStyle("sig", fontName="Arial-BoldItalic", fontSize=22, leading=26, textColor=NAVY)),
        HRFlowable(width=210, thickness=0.8, color=NAVY, spaceBefore=2, spaceAfter=3, hAlign="LEFT"),
        Paragraph("<b>RIVET-CEO</b>, Chief Executive Officer", st["body"]),
        Paragraph("Robots of Doom Incorporated", st["body"]), Paragraph(CFG["date"], st["body"]),
        Spacer(1, 8), Paragraph('<i>"Great debate. Now, what do we do on Monday?"</i>', st["note"]),
        Spacer(1, 14), Paragraph("Board members who contributed", st["H3"]), make_table(board, CW),
        Spacer(1, 16), Paragraph(f"Chairman's ratification of decision {CFG['decision_id']}", st["H3"]),
        Paragraph(CFG["decision_text"], st["body"]), Spacer(1, 6),
        Table([[Paragraph("[   ]  Ratified", st["body"]), Paragraph("[   ]  Vetoed", st["body"]),
                Paragraph("[   ]  Sent back (note which slot or question):", st["body"])]],
              colWidths=[CW * 0.2, CW * 0.2, CW * 0.6]),
        Spacer(1, 22), HRFlowable(width=210, thickness=0.8, color=NAVY, spaceBefore=2, spaceAfter=3, hAlign="LEFT"),
        Paragraph("Caleb, Founder and Chairman. Signature and date.", st["note"])]
story.append(KeepTogether(sign))
doc.multiBuild(story)
print(OUT)
