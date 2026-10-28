#!/usr/bin/env python3
"""Build the current public product manuals as polished PDF artifacts."""

from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Image,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
GOLD = colors.HexColor("#C69A42")
INK = colors.HexColor("#17212B")
MUTED = colors.HexColor("#607080")
PALE = colors.HexColor("#F6F2E8")
LINE = colors.HexColor("#D9E1DC")


def inline_markup(text: str) -> str:
    text = (text.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
            .replace("↔", "<->").replace("→", "->"))
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"<u>\1</u>", text)
    return text


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("title", parent=base["Title"], fontName="Helvetica-Bold", fontSize=25, leading=29, textColor=INK, alignment=TA_CENTER, spaceAfter=8),
        "subtitle": ParagraphStyle("subtitle", parent=base["Normal"], fontName="Helvetica", fontSize=10, leading=14, textColor=MUTED, alignment=TA_CENTER, spaceAfter=14),
        "h1": ParagraphStyle("h1", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=INK, spaceBefore=11, spaceAfter=7, keepWithNext=True),
        "h2": ParagraphStyle("h2", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=GOLD, spaceBefore=9, spaceAfter=5, keepWithNext=True),
        "h3": ParagraphStyle("h3", parent=base["Heading3"], fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=INK, spaceBefore=7, spaceAfter=4, keepWithNext=True),
        "body": ParagraphStyle("body", parent=base["BodyText"], fontName="Helvetica", fontSize=9.2, leading=13.2, textColor=INK, alignment=TA_LEFT, spaceAfter=6),
        "bullet": ParagraphStyle("bullet", parent=base["BodyText"], fontName="Helvetica", fontSize=9.2, leading=13, leftIndent=4, textColor=INK),
        "note": ParagraphStyle("note", parent=base["BodyText"], fontName="Helvetica", fontSize=8.8, leading=12.5, leftIndent=8, rightIndent=8, borderColor=GOLD, borderWidth=0.7, borderPadding=8, backColor=PALE, textColor=INK, spaceBefore=4, spaceAfter=8),
        "table": ParagraphStyle("table", parent=base["BodyText"], fontName="Helvetica", fontSize=7.8, leading=10, textColor=INK),
        "small": ParagraphStyle("small", parent=base["BodyText"], fontName="Helvetica", fontSize=7.5, leading=10, textColor=MUTED),
    }


def parse_manual(path: Path, logo: Path, product: str, version: str):
    st = styles()
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].strip() == "---":
        try:
            end = next(index for index, value in enumerate(lines[1:], start=1) if value.strip() == "---")
            lines = lines[end + 1:]
        except StopIteration:
            pass
    story = [Spacer(1, 12 * mm)]
    if logo.exists():
        img = Image(str(logo))
        max_w, max_h = 150 * mm, 42 * mm
        scale = min(max_w / img.imageWidth, max_h / img.imageHeight)
        img.drawWidth, img.drawHeight = img.imageWidth * scale, img.imageHeight * scale
        img.hAlign = "CENTER"
        story.extend([img, Spacer(1, 8 * mm)])
    story.extend([
        Paragraph(f"{product} operational manual", st["title"]),
        Paragraph(f"Stable release {version} · DukeVilla Data Transmission &amp; Signal Processing", st["subtitle"]),
        Spacer(1, 6 * mm),
        Paragraph("This is the current living operational manual. It covers the stable interface, validated workflows, safety boundaries, maintenance, and recovery.", st["note"]),
        PageBreak(),
    ])

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("---") or line.startswith("![") or line.startswith("[Download"):
            i += 1
            continue
        if line.startswith("# "):
            i += 1
            continue
        if line.startswith("## "):
            story.append(Paragraph(inline_markup(line[3:]), st["h1"]))
            i += 1
            continue
        if line.startswith("### "):
            story.append(Paragraph(inline_markup(line[4:]), st["h2"]))
            i += 1
            continue
        if line.startswith("#### "):
            story.append(Paragraph(inline_markup(line[5:]), st["h3"]))
            i += 1
            continue
        if line.startswith(":::"):
            kind = line[3:].strip()
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(":::"):
                if lines[i].strip():
                    body.append(lines[i].strip())
                i += 1
            i += 1
            label = "WARNING" if kind in {"warning", "danger"} else "NOTE"
            story.append(Paragraph(f"<b>{label}</b><br/>{inline_markup(' '.join(body))}", st["note"]))
            continue
        if line.startswith("|") and i + 1 < len(lines) and set(lines[i + 1].replace("|", "").replace("-", "").replace(":", "").strip()) == set():
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                raw = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
                if not all(set(cell) <= {"-", ":", " "} for cell in raw):
                    rows.append([Paragraph(inline_markup(cell), st["table"]) for cell in raw])
                i += 1
            if rows:
                table = Table(rows, repeatRows=1, hAlign="LEFT")
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), INK), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.white), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]))
                story.extend([table, Spacer(1, 5)])
            continue
        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(ListItem(Paragraph(inline_markup(lines[i].strip()[2:]), st["bullet"]), leftIndent=10))
                i += 1
            story.append(ListFlowable(items, bulletType="bullet", start="circle", leftIndent=16, bulletFontName="Helvetica", bulletFontSize=6, spaceAfter=6))
            continue
        if re.match(r"^\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(ListItem(Paragraph(inline_markup(re.sub(r"^\d+\. ", "", lines[i].strip())), st["bullet"]), leftIndent=12))
                i += 1
            story.append(ListFlowable(items, bulletType="1", leftIndent=18, spaceAfter=6))
            continue
        if line.startswith(">"):
            story.append(Paragraph(inline_markup(line.lstrip("> ")), st["note"]))
            i += 1
            continue
        paragraph = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||- |\d+\. |:::|>|!\[|\[Download)", lines[i].strip()):
            paragraph.append(lines[i].strip())
            i += 1
        story.append(Paragraph(inline_markup(" ".join(paragraph)), st["body"]))
    return story


def draw_page(canvas, doc, product: str, version: str):
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(1.2)
    canvas.line(18 * mm, height - 14 * mm, width - 18 * mm, height - 14 * mm)
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(INK)
    canvas.drawString(18 * mm, height - 10.5 * mm, product)
    canvas.setFont("Helvetica", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(width - 18 * mm, height - 10.5 * mm, f"Stable {version}")
    canvas.line(18 * mm, 13 * mm, width - 18 * mm, 13 * mm)
    canvas.drawString(18 * mm, 8.5 * mm, "DukeVilla · Official operational documentation")
    canvas.drawRightString(width - 18 * mm, 8.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build(source: Path, logo: Path, output: Path, product: str, version: str):
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm, topMargin=20 * mm, bottomMargin=18 * mm, title=f"{product} operational manual", author="DukeVilla")
    story = parse_manual(source, logo, product, version)
    doc.build(story, onFirstPage=lambda c, d: draw_page(c, d, product, version), onLaterPages=lambda c, d: draw_page(c, d, product, version))


if __name__ == "__main__":
    build(ROOT / "docs/traduktor.md", ROOT / "static/img/traduktor-logo.png", ROOT / "static/downloads/traduktor/traDUKtor_Lite_Operational_Manual_0.2.31.pdf", "traDUKtor Lite", "0.2.31")
    build(ROOT / "docs/facil-iot.md", ROOT / "static/img/facil-iot-logo.png", ROOT / "static/downloads/facil-iot/Facil_IoT_Operational_Manual_0.1.18.pdf", "Fácil IoT", "0.1.18")
