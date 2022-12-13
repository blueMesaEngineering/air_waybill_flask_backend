from pymongo import MongoClient
import gridfs

class AWBPDF():
  def put(self):
    airWaybillPDFDB = MongoClient().air_waybill_pdf_db
    fileSystem = gridfs.GridFS(airWaybillPDFDB)
    a = fileSystem.put(b"./assets/air-waybill-form.pdf")