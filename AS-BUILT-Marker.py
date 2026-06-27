# AS-BUILT Marker V1.0 from - https://github.com/Booth-Ashley/As-Built-Marker
# Built by Ashley Booth - https://ashley-booth.com/

import os
import math
from io import BytesIO
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color

def create_watermark(page_width, page_height):
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, page_height))

    text = "AS-BUILT"

    diagonal = math.sqrt(page_width**2 + page_height**2)
    target_width = diagonal * 0.50 * 0.9

    approx_char_factor = 0.6 * len(text)
    font_size = target_width / approx_char_factor

    font_size = max(20, min(font_size, 250))

    c.setFont("Helvetica-Bold", font_size)

    faint_red = Color(1, 0, 0, alpha=0.25)
    c.setFillColor(faint_red)
    c.setStrokeColor(faint_red)

    x = page_width / 2
    y = page_height / 2

    c.saveState()
    c.translate(x, y)
    c.rotate(-45)

    text_width = c.stringWidth(text, "Helvetica-Bold", font_size)
    padding = font_size * 0.25

    c.rect(
        -text_width / 2 - padding,
        -font_size / 2 - padding,
        text_width + 2 * padding,
        font_size + 2 * padding,
        stroke=1,
        fill=0
    )

    c.drawCentredString(0, -font_size / 3, text)

    c.restoreState()
    c.save()

    packet.seek(0)
    return PdfReader(packet).pages[0]


def watermark_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        page_width = float(page.mediabox.width)
        page_height = float(page.mediabox.height)

        watermark = create_watermark(page_width, page_height)
        page.merge_page(watermark)
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)


def batch_watermark(output_folder="AS-BUILT"):
    input_folder = os.getcwd()

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)

            name, ext = os.path.splitext(filename)
            output_filename = f"{name} - AS-BUILT.pdf"
            output_path = os.path.join(output_folder, output_filename)

            print(f"Processing: {filename}")
            watermark_pdf(input_path, output_path)


if __name__ == "__main__":
    batch_watermark()
