from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 100, "Hello World")
can.save()

packet.seek(0)

newPdf = PdfFileReader(packet)
existingPdf = PdfFileReader(open("./assets/air-waybill-form.pdf", "rb"))
output = PdfFileWriter()
page = existingPdf.getPage(0)
page.mergePage(newPdf.getPage(0))
output.addPage(page)

outputStream = open("./assets/output/output-air-waybill-form.pdf", "wb")
output.write(outputStream)
outputStream.close()