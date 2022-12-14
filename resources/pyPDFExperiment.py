from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# payload = [
#   serialNumberAWBPDF = "1043 0894 5389 1062"
# ]

def setUpCanvas():
  packet = io.BytesIO()
  can = canvas.Canvas(packet, pagesize=letter)
  writeSerialNumberAWBPDF(can)
  writeShipper(can)
  writeConsignee(can)
  writeCarrier(can)
  can.save()
  packet.seek(0)
  return packet
  
def writeSerialNumberAWBPDF(can):
  can.setFont('Times-Roman', 8)
  can.drawString(54, 356, "1043 0894 5389 1062")

def writeShipper(can):
  can.setFont('Times-Roman', 4)
  can.drawString(30, 345, "Nathan D. Guthrie")
  can.drawString(30, 341, "Blue Mesa Engineering")
  can.drawString(30, 337, "101 Main St.")
  can.drawString(30, 333, "Ste A")
  can.drawString(30, 329, "Anytown, Oregadaho")

def writeConsignee(can):
  can.setFont('Times-Roman', 4)
  can.drawString(30, 315, "Barry White")
  can.drawString(30, 311, "Jazzersize")
  can.drawString(30, 307, "1 Love Song Lane")
  can.drawString(30, 303, "Ste A")
  can.drawString(30, 299, "Amor, Ciudad")

def writeCarrier(can):
  can.setFont('Times-Roman', 4)
  can.drawString(30, 284, "Huffland Duster")
  can.drawString(30, 280, "Keystone Corp")
  can.drawString(30, 276, "1 Keystone Ave.")
  can.drawString(30, 272, "Macon, GA")

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