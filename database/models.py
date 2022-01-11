from .db import db

class Shipper(db.Document):
  firstName = db.StringField(required=True)
  middleName = db.StringField(required=True)
  lastName = db.StringField(required=True)
  companyName = db.StringField(required=True, unique=True)
  streetAddress1 = db.StringField(required=True)
  streetAddress2 = db.StringField(required=True)
  city = db.StringField(required=True)
  state = db.StringField(required=True)