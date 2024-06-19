import pypdf
from pypdf import Transformation

INPUT_PDF   = "pdf.pdf"
OUTPUT_PDF  = "out.pdf"

# compute scale to target a certaint resolution (?)
SCALE = 0.368

reader = pypdf.PdfReader(INPUT_PDF)
writer = pypdf.PdfWriter()
for page in reader.pages:
    # print(page.mediabox.right, page.mediabox.top)
    op = Transformation().scale(sx=SCALE, sy=SCALE)
    page.add_transformation(op)
    page.mediabox.upper_right = (page.mediabox.right * SCALE, page.mediabox.top * SCALE)
    writer.add_page(page)
    # print(writer.pages[0].mediabox.right, writer.pages[0].mediabox.top)
    
with open(f"{OUTPUT_PDF}", "wb+") as f:
    writer.write(f)


# SHADOWDARK DEMO (1139.76 1618.56)
# RAVENLOFT (597 786)
# SHADOWDARK QUICKSTART (419.528 595.276)
# DELVER ZINE (414 630)