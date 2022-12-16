from .db import db

class AirWaybill(db.Document):
  
  # AWB Serial Number
  serialNumberAWBPDF = db.StringField(required=True)
  
  # Shipper Data
  shipperFirstName = db.StringField(required=True)
  shipperMiddleName = db.StringField(required=True)
  shipperLastName = db.StringField(required=True)
  shipperCompanyName = db.StringField(required=True, unique=True)
  shipperStreetAddress1 = db.StringField(required=True)
  shipperStreetAddress2 = db.StringField(required=True)
  shipperCity = db.StringField(required=True)
  shipperStateUSA = db.StringField(required=True)
  shipperAccordionState = db.StringField(required=True)  
  
  # Consignee Data
  consigneeFirstName = db.StringField(required=True)
  consigneeMiddleName = db.StringField(required=True)
  consigneeLastName = db.StringField(required=True)
  consigneeCompanyName = db.StringField(required=True, unique=True)
  consigneeStreetAddress1 = db.StringField(required=True)
  consigneeStreetAddress2 = db.StringField(required=True)
  consigneeCity = db.StringField(required=True)
  consigneeStateUSA = db.StringField(required=True)
  consigneeAccordionState = db.BooleanField(required=True, default=False)
  
  # Carrier Data
  carrierFirstName = db.StringField(required=True)
  carrierMiddleName = db.StringField(required=True)
  carrierLastName = db.StringField(required=True)
  carrierCompanyName = db.StringField(required=True, unique=True)
  carrierStreetAddress1 = db.StringField(required=True)
  carrierStreetAddress2 = db.StringField(required=True)
  carrierCity = db.StringField(required=True)
  carrierStateUSA = db.StringField(required=True)
  carrierAccordionState = db.BooleanField(required=True, default=False)
  
class Shipper(db.Document):
  shipperFirstName = db.StringField(required=True)
  shipperMiddleName = db.StringField(required=True)
  shipperLastName = db.StringField(required=True)
  shipperCompanyName = db.StringField(required=True, unique=True)
  shipperStreetAddress1 = db.StringField(required=True)
  shipperStreetAddress2 = db.StringField(required=True)
  shipperCity = db.StringField(required=True)
  shipperStateUSA = db.StringField(required=True)
  shipperAccordionState = db.BooleanField(required=True, default=False)
  
class Consignee(db.Document):
  consigneeFirstName = db.StringField(required=True)
  consigneeMiddleName = db.StringField(required=True)
  consigneeLastName = db.StringField(required=True)
  consigneeCompanyName = db.StringField(required=True, unique=True)
  consigneeStreetAddress1 = db.StringField(required=True)
  consigneeStreetAddress2 = db.StringField(required=True)
  consigneeCity = db.StringField(required=True)
  consigneeStateUSA = db.StringField(required=True)
  consigneeAccordionState = db.BooleanField(required=True, default=False)
  
class Carrier(db.Document):
  carrierFirstName = db.StringField(required=True)
  carrierMiddleName = db.StringField(required=True)
  carrierLastName = db.StringField(required=True)
  carrierCompanyName = db.StringField(required=True, unique=True)
  carrierStreetAddress1 = db.StringField(required=True)
  carrierStreetAddress2 = db.StringField(required=True)
  carrierCity = db.StringField(required=True)
  carrierStateUSA = db.StringField(required=True)
  carrierAccordionState = db.BooleanField(required=True, default=False)
  
class ShipperSearch(db.Document):
  shipperFirstName = db.StringField(required=True)
  shipperID = db.StringField(required=True)

class AirWaybillPDFCrossRef(db.Document):
  airWaybillSerialNumber = db.StringField(required=True)
  airWaybillPDFID = db.StringField(required=True)