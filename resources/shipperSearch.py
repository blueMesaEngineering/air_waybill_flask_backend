import pymongo
# import datetime
# import pprint
from flask import Response, request
from database.models import Shipper
from flask_restful import Resource
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.air_waybill_flask_backend
shippers = db.shippers

class ShipperSearchAPI(Resource):
  def get(query):
    cursor = shippers.find({"shipperFirstName": query})
    temp = getShippersByFirstName(cursor)
    
    return temp

def getShippersByFirstName(cursor):
  selectedShippers = []

  for shipper in cursor:
    selectedShippers.append(shipper)

  return selectedShippers