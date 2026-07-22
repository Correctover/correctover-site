#!/usr/bin/env python3
"""Generate Correctover One-Pager PDF (print-ready, A4, dark theme)."""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

OUTPUT = r"C:\d\workspace\correctover\web\assets\Correctover-One-Pager.pdf"
W, H = A4

# ── Colors ─────────────────────────────────────────────────────────────────
BG          = HexColor("#08080f")
ACCENT      = HexColor("#00d4b0")
WHITE       = white
GRAY        = HexColor("#888899")
DARK_CARD   = HexColor("#0e0e18")
DARK_TH     = HexColor("#14142a")
GRAY_LIGHT  = HexColor("#ccccdd")
GRAY_DIM    = HexColor("#aaaaaa")
GRAY_MUTED  = HexColor("#555566")
DIVIDER     = HexColor("#1a1a2a")

def hex_to_rgb(h):
    return h.red, h.green, h.blue

BG_RGB = hex_to_rgb(BG)

def background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    # top accent line
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(2)
    canvas.line(0, H - 1, W, H - 1)
    canvas.restoreState()

# ── Styles ─────────────────────────────────────────────────────────────────
FONTR = "Helvetica"
FONTB = "Helvetica-Bold"

s_comp = ParagraphStyle("C", fontName=FONTB, fontSize=28, textColor=WHITE,
    alignment=TA_CENTER, leading=34, spaceAfter=1*mm)
s_tag  = ParagraphStyle("T", fontName=FONTR, fontSize=11, textColor=ACCENT,
    alignment=TA_CENTER, leading=15, spaceAfter=0)
s_sn   = ParagraphStyle("SN", fontName=FONTB, fontSize=20, textColor=ACCENT,
    alignment=TA_CENTER, leading=24)
s_sl   = ParagraphStyle("SL", fontName=FONTR, fontSize=8, textColor=GRAY,
    alignment=TA_CENTER, leading=10)
s_sec  = ParagraphStyle("S", fontName=FONTB, fontSize=12, textColor=WHITE,
    alignment=TA_LEFT, leading=15, spaceAfter=2*mm)
s_pt   = ParagraphStyle("PT", fontName=FONTB, fontSize=10, textColor=WHITE,
    alignment=TA_LEFT, leading=13, spaceAfter=1*mm)
s_pb   = ParagraphStyle("PB", fontName=FONTR, fontSize=7.5, textColor=GRAY_LIGHT,
    alignment=TA_LEFT, leading=10, spaceAfter=0)
s_th   = ParagraphStyle("TH", fontName=FONTB, fontSize=7, textColor=ACCENT,
    alignment=TA_LEFT, leading=9)
s_tc   = ParagraphStyle("TC", fontName=FONTR, fontSize=7, textColor=GRAY_LIGHT,
    alignment=TA_LEFT, leading=9)
s_tcc  = ParagraphStyle("TCC", fontName=FONTR, fontSize=7, textColor=GRAY_LIGHT,
    alignment=TA_CENTER, leading=9)
s_dt   = ParagraphStyle("DT", fontName=FONTB, fontSize=8, textColor=WHITE,
    alignment=TA_CENTER, leading=10)
s_di   = ParagraphStyle("DI", fontName=FONTR, fontSize=7, textColor=GRAY_DIM,
    alignment=TA_CENTER, leading=9)
s_pr   = ParagraphStyle("PR", fontName=FONTR, fontSize=8, textColor=GRAY,
    alignment=TA_CENTER, leading=11)
s_ce   = ParagraphStyle("CE", fontName=FONTB, fontSize=10, textColor=ACCENT,
    alignment=TA_CENTER, leading=14)
s_cw   = ParagraphStyle("CW", fontName=FONTR, fontSize=8, textColor=GRAY,
    alignment=TA_CENTER, leading=11)
s_dis  = ParagraphStyle("DI", fontName=FONTR, fontSize=5.5, textColor=GRAY_MUTED,
    alignment=TA_CENTER, leading=7)

# ── Build Story ────────────────────────────────────────────────────────────
story = []
story.append(Spacer(1, 8*mm))

# Header
story.append(Paragraph("CORRECTOVER", s_comp))
story.append(Paragraph("AI Runtime Security", s_tag))
story.append(Spacer(1, 4*mm))

# Stats bar
stats_data = [
    [Paragraph("14.5<font color='#888899' size='9'>µs</font>", s_sn),
     Paragraph("24", s_sn),
     Paragraph("80K", s_sn),
     Paragraph("4,709", s_sn)],
    [Paragraph("P50 Latency", s_sl),
     Paragraph("CCS Detection Rules", s_sl),
     Paragraph("Production Traces", s_sl),
     Paragraph("Validated Findings", s_sl)],
]
st = Table(stats_data, colWidths=[47*mm]*4, rowHeights=[8*mm, 5*mm])
st.setStyle(TableStyle([
    ("ALIGN", (0,0),(-1,-1),"CENTER"),
    ("VALIGN", (0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING", (0,0),(-1,0),0),
    ("BOTTOMPADDING", (0,0),(-1,0),0),
    ("TOPPADDING", (0,1),(-1,1),0),
    ("BOTTOMPADDING", (0,1),(-1,1),1.5*mm),
    ("LEFTPADDING", (0,0),(-1,-1),0),
    ("RIGHTPADDING", (0,0),(-1,-1),0),
    ("LINEAFTER", (0,0),(2,-1),0.5,DIVIDER),
    ("LINEBEFORE", (1,0),(1,-1),0.5,DIVIDER),
]))
sc = Table([[st]], colWidths=[W - 24*mm])
sc.setStyle(TableStyle([
    ("BACKGROUND", (0,0),(-1,-1),DARK_CARD),
    ("TOPPADDING", (0,0),(-1,-1),2*mm),
    ("BOTTOMPADDING", (0,0),(-1,-1),0),
    ("LEFTPADDING", (0,0),(-1,-1),12*mm),
    ("RIGHTPADDING", (0,0),(-1,-1),12*mm),
]))
story.append(sc)
story.append(Spacer(1, 5*mm))

# Product Capabilities
story.append(Paragraph("PRODUCT CAPABILITIES", s_sec))

pillars_data = [
    [Paragraph(
        '<font color="#00d4b0">⚠</font>  <font color="#ffffff">Real-time Detection</font>',
        s_pt),
     Paragraph(
        '<font color="#00d4b0">⛨</font>  <font color="#ffffff">Zero-Day Coverage</font>',
        s_pt),
     Paragraph(
        '<font color="#00d4b0">⚖</font>  <font color="#ffffff">Compliance Ready</font>',
        s_pt)],
    [Paragraph(
        "Inline runtime detection at 14.5µs P50 latency. "
        "7 rule categories: RCE, SSRF, Credential Exfiltration, "
        "Path Traversal, Prompt Injection, Supply Chain Tampering, "
        "Data Exfiltration. 24 CCS-aligned rules.", s_pb),
     Paragraph(
        "Validated across 13 providers and 33 models on 80K "
        "production traces. 6 RCE vulnerabilities discovered "
        "and disclosed: CrewAI, AutoGen Studio, Docker MCP, "
        "AG2, LlamaIndex, and Haystack.", s_pb),
     Paragraph(
        "CCS framework alignment. Automatic SOC2 / ISO27001 "
        "evidence generation. Audit-ready compliance reports "
        "for enterprise requirements.", s_pb)],
]

ptable = Table(pillars_data, colWidths=[56*mm]*3)
ptable.setStyle(TableStyle([
    ("VALIGN", (0,0),(-1,-1),"TOP"),
    ("TOPPADDING", (0,0),(-1,0),1*mm),
    ("BOTTOMPADDING", (0,0),(-1,0),0),
    ("TOPPADDING", (0,1),(-1,1),1*mm),
    ("BOTTOMPADDING", (0,1),(-1,1),2*mm),
    ("LEFTPADDING", (0,0),(-1,-1),2*mm),
    ("RIGHTPADDING", (0,0),(-1,-1),2*mm),
    ("BACKGROUND", (0,0),(0,-1),DARK_CARD),
    ("BACKGROUND", (1,0),(1,-1),DARK_CARD),
    ("BACKGROUND", (2,0),(2,-1),DARK_CARD),
    ("LINEBELOW", (0,0),(0,0),2,ACCENT),
    ("LINEBELOW", (1,0),(1,0),2,ACCENT),
    ("LINEBELOW", (2,0),(2,0),2,ACCENT),
    ("LEFTPADDING", (1,0),(1,-1),3*mm),
    ("RIGHTPADDING", (0,0),(0,-1),3*mm),
    ("RIGHTPADDING", (1,0),(1,-1),3*mm),
    ("LEFTPADDING", (2,0),(2,-1),3*mm),
]))
story.append(ptable)

# Bounty Track Record
story.append(Spacer(1, 4*mm))
story.append(Paragraph("BOUNTY TRACK RECORD", s_sec))

vuln_header = [
    Paragraph("Vulnerability", s_th),
    Paragraph("Product", s_th),
    Paragraph("Type", s_th),
    Paragraph("Program", s_th),
]
vuln_rows = [
    [Paragraph("CrewAI MCP RCE", s_tc), Paragraph("CrewAI", s_tc),
     Paragraph("RCE", s_tcc), Paragraph("MSRC", s_tcc)],
    [Paragraph("AutoGen Studio RCE", s_tc), Paragraph("AutoGen", s_tc),
     Paragraph("RCE (CVSS 9.8)", s_tcc), Paragraph("ZDI", s_tcc)],
    [Paragraph("Docker MCP Container Escape", s_tc), Paragraph("Docker MCP", s_tc),
     Paragraph("Escape", s_tcc), Paragraph("GitHub", s_tcc)],
    [Paragraph("LiteLLM SSRF", s_tc), Paragraph("LiteLLM", s_tc),
     Paragraph("SSRF", s_tcc), Paragraph("GitHub", s_tcc)],
    [Paragraph("AG2 Pickle RCE", s_tc), Paragraph("AG2", s_tc),
     Paragraph("RCE", s_tcc), Paragraph("GitHub", s_tcc)],
    [Paragraph("Haystack Pipeline RCE", s_tc), Paragraph("Haystack", s_tc),
     Paragraph("RCE", s_tcc), Paragraph("GitHub", s_tcc)],
]

vt = Table([vuln_header] + vuln_rows, colWidths=[42*mm, 28*mm, 28*mm, 24*mm])
vt.setStyle(TableStyle([
    ("BACKGROUND", (0,0),(-1,0),DARK_TH),
    ("TEXTCOLOR", (0,0),(-1,0),ACCENT),
    ("ALIGN", (0,0),(-1,-1),"LEFT"),
    ("VALIGN", (0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING", (0,0),(-1,-1),1.2*mm),
    ("BOTTOMPADDING", (0,0),(-1,-1),1.2*mm),
    ("LEFTPADDING", (0,0),(-1,-1),1.5*mm),
    ("RIGHTPADDING", (0,0),(-1,-1),1.5*mm),
    ("GRID", (0,0),(-1,-1),0.5,DIVIDER),
    ("LINEABOVE", (0,0),(-1,0),1.5,ACCENT),
]))
story.append(vt)

# Deployment
story.append(Spacer(1, 4*mm))
story.append(Paragraph("DEPLOYMENT OPTIONS", s_sec))

deploy_items = [
    [Paragraph("MCP Protocol", s_dt), Paragraph("Python SDK", s_dt),
     Paragraph("npm Package", s_dt), Paragraph("Docker", s_dt),
     Paragraph("Cloudflare Workers", s_dt), Paragraph("Render.com", s_dt)],
    [Paragraph("Standard MCP\nserver integration", s_di),
     Paragraph("pip install\ncorrectover", s_di),
     Paragraph("npm install\n@correctover/sdk", s_di),
     Paragraph("docker pull\ncorrectover/gateway", s_di),
     Paragraph("Edge runtime\nprotection", s_di),
     Paragraph("Managed cloud\nhosting", s_di)],
]

dt = Table(deploy_items, colWidths=[27*mm]*6)
dt.setStyle(TableStyle([
    ("ALIGN", (0,0),(-1,-1),"CENTER"),
    ("VALIGN", (0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING", (0,0),(-1,-1),1.5*mm),
    ("BOTTOMPADDING", (0,0),(-1,-1),1.5*mm),
    ("LEFTPADDING", (0,0),(-1,-1),1*mm),
    ("RIGHTPADDING", (0,0),(-1,-1),1*mm),
    ("BACKGROUND", (0,0),(0,-1),DARK_CARD),
    ("BACKGROUND", (1,0),(1,-1),DARK_CARD),
    ("BACKGROUND", (2,0),(2,-1),DARK_CARD),
    ("BACKGROUND", (3,0),(3,-1),DARK_CARD),
    ("BACKGROUND", (4,0),(4,-1),DARK_CARD),
    ("BACKGROUND", (5,0),(5,-1),DARK_CARD),
    ("LEFTPADDING", (1,0),(1,-1),1.5*mm),
    ("RIGHTPADDING", (0,0),(0,-1),1.5*mm),
]))
story.append(dt)

# Pricing + Contact
story.append(Spacer(1, 3*mm))
story.append(Paragraph(
    "Free Trial (7d) &nbsp;·&nbsp; Pro Monthly ¥99 &nbsp;·&nbsp; "
    "Pro Annual ¥699 &nbsp;·&nbsp; Team ¥499/mo",
    s_pr))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("wangguigui@correctover.com", s_ce))
story.append(Paragraph("https://correctover.com/en", s_cw))
story.append(Spacer(1, 2*mm))
story.append(Paragraph(
    "Correctover — AI Runtime Security. CCS Framework aligned. "
    "Safeguarding AI agents in production.", s_dis))

# ── Build PDF ──────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=12*mm, rightMargin=12*mm,
    topMargin=15*mm, bottomMargin=15*mm,
    title="Correctover - AI Runtime Security One-Pager",
    author="Correctover Security",
    subject="Product Overview",
)
doc.build(story, onFirstPage=background, onLaterPages=background)

size = os.path.getsize(OUTPUT)
print(f"PDF created: {OUTPUT}")
print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")
assert size > 0, "PDF file is empty!"
print("Verification: PASSED")
