# PDF Text Extractor
# pip install pypdfium2
import pypdfium2 as pypdf
def Extract_Text(pdf_file):
    pdf = pypdf.PdfDocument(pdf_file)
    num_pages = len(pdf)
    text = ""
    for p in range(num_pages):
        page = pdf[p]
        temp = page.get_textpage()
        text = text + temp.get_text_range() + " "
    print("PDF TEXT: ", text)
Extract_Text('test12.pdf')