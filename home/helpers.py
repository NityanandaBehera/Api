from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import uuid

def save_pdf(params:dict):
    template=get_template("pdf.html")
    html=template.render(params)
    pdf=pisa.pisaDocument(BytesIO(html.encode('UTF-8')),response)