from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def setUpCanvas():
  packet = io.BytesIO()
  can = canvas.Canvas(packet, pagesize=letter)
  writeSerialNumberAWBPDF(can)
  writeShipper(can)
  writeConsignee(can)
  can.save()
  packet.seek(0)
  return packet
  
def writeSerialNumberAWBPDF(can):
  can.setFont('Times-Roman', 8)
  can.drawString(54, 356, "1043 0894 5389 1062")

def writeShipper(can):
  can.setFont('Times-Roman', 5)
  can.drawString(30, 345, "Nathan D. Guthrie")
  can.drawString(30, 340, "Blue Mesa Engineering")
  can.drawString(30, 335, "101 Main St.")
  can.drawString(30, 330, "Ste A")
  can.drawString(30, 325, "Oregadaho, USA")

def writeConsignee(can):
  can.drawString(30, 315, "Barry White")
  can.drawString(30, 310, "Jazzersize")
  can.drawString(30, 305, "1 Love Song Lane")
  can.drawString(30, 300, "Ste A")
  can.drawString(30, 295, "Oregadaho, USA")

packet = setUpCanvas()

newPdf = PdfFileReader(packet)
existingPdf = PdfFileReader(open("./assets/air-waybill-form.pdf", "rb"))
output = PdfFileWriter()
page = existingPdf.getPage(0)
page.mergePage(newPdf.getPage(0))
output.addPage(page)

outputStream = open("./assets/output/output-air-waybill-form.pdf", "wb")
output.write(outputStream)
outputStream.close()