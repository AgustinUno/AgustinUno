"""Build the resume as DOCX (python-docx) and PDF (reportlab) from one content model.

Usage:
    pip install python-docx reportlab
    python tools/build_resume.py

Writes resume/Justine-Lloyd-Bautista-Resume.docx and .pdf. Edit the content constants
below, not the generated files.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "resume")
os.makedirs(OUT, exist_ok=True)

NAME = "Justine Lloyd Bautista"
ROLE = "Software Developer  \u00b7  UI/UX & Visual Designer"
CONTACT = [
    "justinelloydgbautista.pupsj@gmail.com",
    "linkedin.com/in/justine-lloyd-bautista-666432228",
    "github.com/AgustinUno",
    "Philippines",
]
SUMMARY = (
    "Design-driven full-stack engineer with 9+ years in visual design, shipping data-critical internal "
    "tools for a PhilHealth-accredited health IT provider. Bridges clinical accuracy with interface "
    "clarity: systems processing 50,000+ validation rows per run, and real-time collaborative editing "
    "with live presence \u2014 for 2,000+ healthcare units nationwide."
)

EXPERIENCE = [
    {
        "role": "Software Developer",
        "org": "Eurolink Network International Corp.",
        "when": "2026",
        "bullets": [
            "Built a browser-native Claims XML validation engine processing 50,000+ rows per run, "
            "replacing a fatal Chromium memory ceiling with a compact columnar pipeline \u2014 keeping "
            "reconciliation exact.",
            "Shipped real-time collaborative notes (Tiptap, Yjs, SignalR) with role-based access control "
            "and live caret tracking, modelled on Notion's editing experience.",
            "Delivered internal MIS modules for one of seven PhilHealth-accredited HITPs in the "
            "Philippines, serving 2,000+ healthcare units.",
        ],
    },
    {
        "role": "Full-Stack Developer",
        "org": "PUP San Juan \u2014 Quality Assurance Office",
        "when": "2023 \u2013 2026",
        "bullets": [
            "Built and maintained digital accreditation workflows (Laravel, PostgreSQL) covering the full "
            "document evaluation cycle.",
            "Owned UI/UX architecture and technical support, streamlining evaluation across the university.",
        ],
    },
    {
        "role": "VP for Communications & Lead Designer",
        "org": "GLITCH & Student Council",
        "when": "2022 \u2013 Present",
        "bullets": [
            "Directed visual identity, creative teams, and campaign systems for three consecutive years.",
        ],
    },
]

WORK = [
    ("PUPSJ-CON \u2014 Accreditation Platform", "Laravel \u00b7 PostgreSQL \u00b7 Tailwind CSS \u00b7 Figma",
     "Best Capstone Award, PUP San Juan."),
    ("Project V \u2014 Vaccine Management", "Java \u00b7 PHP \u00b7 MySQL",
     "Top 1 Best Project, Asia Pacific College bootcamp."),
    ("ENIC Healthcare MIS Suite", "ASP.NET Core \u00b7 SignalR \u00b7 Tiptap \u00b7 Yjs \u00b7 XML",
     "Production modules for claims validation and collaborative notes; under NDA."),
    ("YAKAP \u2014 Partner Platform Identity", "Figma \u00b7 Design Systems \u00b7 Typography",
     "Brand and interface direction for a PhilHealth-integrated partner platform."),
]

EDUCATION = {
    "degree": "BS Information Technology",
    "school": "Polytechnic University of the Philippines \u2014 San Juan",
    "honors": [
        "Magna Cum Laude, GPA 1.2 (PH scale)",
        "Rank 1, IT graduate \u2014 Rank 3 campus-wide",
        "Junior Programmer of the Year \u00b7 Best Capstone \u00b7 Public Service Award",
    ],
}

CERTS = [
    "Lean Six Sigma Yellow Belt",
    "Fortinet Associate Cybersecurity",
    "FortiGate 7.6 Operator",
    "Cisco Cyber Threat Management",
    "Salesforce Virtual Internship",
    "DTI Graphic Design for SMB & Marketing",
]

SKILLS = [
    ("Languages", "TypeScript, JavaScript, PHP, Java, SQL"),
    ("Frameworks", "React, Laravel, ASP.NET Core (.NET 10), Tailwind CSS"),
    ("Data", "PostgreSQL, MySQL"),
    ("Platform", "Git, Docker, Linux (Debian, RHEL, Arch)"),
    ("Design", "Figma, design systems, typography, brand"),
]

RED = (0xE0, 0x24, 0x4E)
INK = (0x1A, 0x16, 0x18)
MUTED = (0x6B, 0x62, 0x66)
RULE = (0xD9, 0xD2, 0xD4)

DASH = "\u2014"


# --------------------------------------------------------------------------- DOCX
def build_docx(path):
    from docx import Document
    from docx.enum.text import WD_TAB_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Mm, Pt, RGBColor

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)
    sec.top_margin = Cm(1.35)
    sec.bottom_margin = Cm(1.3)
    sec.left_margin = Cm(1.75)
    sec.right_margin = Cm(1.75)
    text_width = sec.page_width - sec.left_margin - sec.right_margin

    style = doc.styles["Normal"]
    style.font.name = "Segoe UI"
    style.font.size = Pt(9.5)
    style.font.color.rgb = RGBColor(*INK)
    style.paragraph_format.space_before = Pt(0)
    style.paragraph_format.space_after = Pt(0)
    style.paragraph_format.line_spacing = 1.06

    def border(par, color, size=6, space=4):
        pPr = par._p.get_or_add_pPr()
        pBdr = OxmlElement("w:pBdr")
        bottom = OxmlElement("w:bottom")
        bottom.set(qn("w:val"), "single")
        bottom.set(qn("w:sz"), str(size))
        bottom.set(qn("w:space"), str(space))
        bottom.set(qn("w:color"), color)
        pBdr.append(bottom)
        pPr.append(pBdr)

    def para(text="", size=9.5, bold=False, color=INK, before=0, after=0,
             spacing=None, caps=False, italic=False):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        run = p.add_run(text)
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = RGBColor(*color)
        if caps:
            run.font.all_caps = True
        if spacing is not None:
            rPr = run._element.get_or_add_rPr()
            sp = OxmlElement("w:spacing")
            sp.set(qn("w:val"), str(int(spacing * 20)))
            rPr.append(sp)
        return p

    para(NAME, size=23, bold=True, spacing=-0.4, after=2)
    para(ROLE, size=10, color=RED, after=5, spacing=0.2)
    p2 = para("   \u00b7   ".join(CONTACT), size=8, color=MUTED, after=9)
    border(p2, "E0244E", size=10, space=8)

    def section(title, before=11):
        s = para(title, size=8.5, bold=True, color=RED, before=before, after=3, caps=True, spacing=1.1)
        border(s, "D9D2D4", size=4, space=3)

    def entry(role, org, when):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(5)
        pf.space_after = Pt(1)
        pf.tab_stops.add_tab_stop(text_width, WD_TAB_ALIGNMENT.RIGHT)
        r = p.add_run(role)
        r.font.size = Pt(10)
        r.font.bold = True
        r2 = p.add_run("\t" + when)
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = RGBColor(*MUTED)
        para(org, size=8.5, color=MUTED, italic=True, after=2)

    def bullet(text):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent = Cm(0.42)
        pf.first_line_indent = Cm(-0.42)
        pf.space_after = Pt(1.5)
        r = p.add_run(DASH + "  ")
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(*RED)
        r2 = p.add_run(text)
        r2.font.size = Pt(9)

    section("Profile", before=2)
    para(SUMMARY, size=9, after=0)

    section("Experience")
    for job in EXPERIENCE:
        entry(job["role"], job["org"], job["when"])
        for b in job["bullets"]:
            bullet(b)

    section("Selected Work")
    for title, stack, note in WORK:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(title)
        r.font.size = Pt(9)
        r.font.bold = True
        r2 = p.add_run("  " + stack)
        r2.font.size = Pt(8)
        r2.font.color.rgb = RGBColor(*RED)
        p.add_run("\n")
        r3 = p.add_run(note)
        r3.font.size = Pt(8.5)
        r3.font.color.rgb = RGBColor(*MUTED)

    section("Education & Honors")
    entry(EDUCATION["degree"], EDUCATION["school"], "2026")
    for h in EDUCATION["honors"]:
        bullet(h)

    section("Certifications & Competitions")
    para("  \u00b7  ".join(CERTS), size=8.5, after=3)
    para("Trend Micro Capture the Flag 2025 \u2014 80th nationwide, Linux exploitation and defensive security.",
         size=8.5, color=MUTED)

    section("Skills")
    for label, value in SKILLS:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1.5)
        r = p.add_run(label + "   ")
        r.font.size = Pt(8.5)
        r.font.bold = True
        r2 = p.add_run(value)
        r2.font.size = Pt(8.5)

    doc.save(path)


# ---------------------------------------------------------------------------- PDF
def build_pdf(path):
    from reportlab import rl_config

    # Fixed creation date and document ID, so rebuilding does not produce a diff.
    rl_config.invariant = 1

    from reportlab.lib import colors
    from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageTemplate,
                                    Paragraph, Spacer, Table, TableStyle)

    fonts = {
        "Segoe": "C:/Windows/Fonts/segoeui.ttf",
        "Segoe-Bold": "C:/Windows/Fonts/segoeuib.ttf",
        "Segoe-Italic": "C:/Windows/Fonts/segoeuii.ttf",
    }
    for key, f in fonts.items():
        try:
            pdfmetrics.registerFont(TTFont(key, f))
        except Exception:
            pass

    def col(rgb):
        return colors.Color(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)

    red, ink, muted, rule = col(RED), col(INK), col(MUTED), col(RULE)

    body = ParagraphStyle("body", fontName="Segoe", fontSize=9.2, leading=12.9, textColor=ink,
                          alignment=TA_LEFT)
    small = ParagraphStyle("small", parent=body, fontSize=8.5, leading=11.4, textColor=muted,
                           alignment=TA_LEFT)
    role_style = ParagraphStyle("role", parent=body, fontName="Segoe-Bold", fontSize=10,
                                leading=13, alignment=TA_LEFT)
    when_style = ParagraphStyle("when", parent=role_style, fontName="Segoe", fontSize=8.5,
                                textColor=muted)
    bullet_style = ParagraphStyle("bullet", parent=body, fontSize=9.1, leading=12.7,
                                  leftIndent=9, alignment=TA_LEFT, spaceAfter=1.2,
                                  bulletFontName="Segoe-Bold", bulletFontSize=9,
                                  bulletColor=red, bulletIndent=0)

    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=17.5 * mm, rightMargin=17.5 * mm,
                          topMargin=13.5 * mm, bottomMargin=12 * mm,
                          title="Justine Lloyd Bautista - Resume", author=NAME)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="page", frames=[frame])])

    story = []
    width = doc.width

    story.append(Paragraph(f"<b>{NAME}</b>", ParagraphStyle(
        "name", parent=body, fontName="Segoe-Bold", fontSize=23, leading=27)))
    story.append(Spacer(1, 3))
    story.append(Paragraph(f"<font color='#E0244E'>{ROLE}</font>", ParagraphStyle(
        "roleln", parent=body, fontSize=10, leading=13)))
    story.append(Spacer(1, 3))
    contact = "   \u00b7   ".join(CONTACT)
    story.append(Paragraph(f"<font size='8' color='#6B6266'>{contact}</font>",
                           ParagraphStyle("contact", parent=body, fontSize=8, leading=11)))
    story.append(Spacer(1, 4))

    rule_tbl = Table([[""]], colWidths=[width], rowHeights=[1.2])
    rule_tbl.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1.4, red),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    story.append(rule_tbl)

    def heading(text, top=9):
        story.append(Spacer(1, top))
        story.append(Paragraph(f"<font color='#E0244E'><b>{text.upper()}</b></font>",
                               ParagraphStyle("h", parent=body, fontSize=8, leading=10)))
        t = Table([[""]], colWidths=[width], rowHeights=[1])
        t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.5, rule),
                               ("TOPPADDING", (0, 0), (-1, -1), 0),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
        story.append(t)
        story.append(Spacer(1, 4))

    heading("Profile", top=8)
    story.append(Paragraph(SUMMARY, body))

    heading("Experience")
    for i, job in enumerate(EXPERIENCE):
        head = Table([[Paragraph(job["role"], role_style), Paragraph(job["when"], when_style)]],
                     colWidths=[width * 0.74, width * 0.26])
        head.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                                  ("VALIGN", (0, 0), (-1, -1), "TOP")]))
        block = [head, Paragraph(f"<i>{job['org']}</i>", small), Spacer(1, 3)]
        for b in job["bullets"]:
            block.append(Paragraph(b, bullet_style, bulletText=DASH))
        story.append(KeepTogether(block))
        if i < len(EXPERIENCE) - 1:
            story.append(Spacer(1, 2))

    heading("Selected Work")
    for title, stack, note in WORK:
        story.append(Paragraph(
            f"<b>{title}</b>  <font size='8' color='#E0244E'>{stack}</font>", body))
        story.append(Paragraph(f"<font size='8.5'>{note}</font>", small))
        story.append(Spacer(1, 1.6))

    heading("Education & Honors")
    head = Table([[Paragraph(EDUCATION["degree"], role_style), Paragraph("2026", when_style)]],
                 colWidths=[width * 0.74, width * 0.26])
    head.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 0),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                              ("ALIGN", (1, 0), (1, 0), "RIGHT")]))
    story.append(head)
    story.append(Paragraph(f"<i>{EDUCATION['school']}</i>", small))
    story.append(Spacer(1, 2))
    for h in EDUCATION["honors"]:
        story.append(Paragraph(h, bullet_style, bulletText=DASH))

    heading("Certifications & Competitions")
    story.append(Paragraph("  \u00b7  ".join(CERTS), small))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "Trend Micro Capture the Flag 2025 \u2014 80th nationwide, Linux exploitation and defensive security.",
        small))

    heading("Skills")
    rows = [[Paragraph(f"<b>{label}</b>", small), Paragraph(value, body)] for label, value in SKILLS]
    t = Table(rows, colWidths=[26 * mm, width - 26 * mm])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0.5),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(t)

    doc.build(story)


if __name__ == "__main__":
    docx_path = os.path.join(OUT, "Justine-Lloyd-Bautista-Resume.docx")
    pdf_path = os.path.join(OUT, "Justine-Lloyd-Bautista-Resume.pdf")
    build_docx(docx_path)
    print("docx:", docx_path)
    try:
        build_pdf(pdf_path)
        print("pdf:", pdf_path)
    except Exception as exc:  # noqa: BLE001
        print("pdf failed:", type(exc).__name__, exc, file=sys.stderr)
