from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# payload = [
#   serialNumberAWBPDF = "1043 0894 5389 1062"
# ]

shipperFirstName = "Nathan"
shipperMiddleName = ""
shipperLastName = "Guthrie"
shipperCompanyName = "Blue Mesa Engineering"
shipperStreetAddress1 = "101 Main St."
shipperStreetAddress2 = "Ste A"
shipperCity = "Anytown"
shipperState = "Oregadaho"

consigneeFirstName = "Barry"
consigneeMiddleName = ""
consigneeLastName = "White"
consigneeCompanyName = "Jazzersize"
consigneeStreetAddress1 = "1 Love Song Lane"
consigneeStreetAddress2 = "Ste A"
consigneeCity = "Amor"
consigneeState = "Ciudad"

carrierFirstName = "Huffland"
carrierMiddleName = ""
carrierLastName = "Duster"
carrierCompanyName = "Keystone Corp"
carrierStreetAddress1 = "1 Keystone Ave."
carrierStreetAddress2 = ""
carrierCity = "Macon"
carrierState = "GA"


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
  if(shipperMiddleName != ""):
    shipperName = shipperFirstName + " " + shipperMiddleName + " " + shipperLastName
  else:
    shipperName = shipperFirstName + " " + shipperLastName
  can.drawString(30, 345, shipperName)
  can.drawString(30, 341, shipperCompanyName)
  can.drawString(30, 337, shipperStreetAddress1)
  if(shipperStreetAddress2 != ""):
    can.drawString(30, 333, shipperStreetAddress2)
  can.drawString(30, 329, shipperCity + ", " + shipperState)

def writeConsignee(can):
  can.setFont('Times-Roman', 4)
  if(consigneeMiddleName != ""):
    consigneeName = consigneeFirstName + " " + consigneeMiddleName + " " + consigneeLastName
  else:
    consigneeName = consigneeFirstName + " " + consigneeLastName
  can.drawString(30, 345, consigneeName)
  can.drawString(30, 341, consigneeCompanyName)
  can.drawString(30, 337, consigneeStreetAddress1)
  if(consigneeStreetAddress2 != ""):
    can.drawString(30, 333, consigneeStreetAddress2)
  can.drawString(30, 329, consigneeCity + ", " + consigneeState)

def writeCarrier(can):
  can.setFont('Times-Roman', 4)
  if(carrierMiddleName != ""):
    carrierName = carrierFirstName + " " + carrierMiddleName + " " + carrierLastName
  else:
    carrierName = carrierFirstName + " " + carrierLastName
  can.drawString(30, 345, carrierName)
  can.drawString(30, 341, carrierCompanyName)
  can.drawString(30, 337, carrierStreetAddress1)
  if(carrierStreetAddress2 != ""):
    can.drawString(30, 333, carrierStreetAddress2)
  can.drawString(30, 329, carrierCity + ", " + carrierState)

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