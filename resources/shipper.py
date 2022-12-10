from flask import Response, request
from database.models import Shipper
from flask_restful import Resource
from database.models import ShipperSearch
import logging
import sys


logger = logging.getLogger('werkzeug') 
handler = logging.FileHandler('test.log') 
logger.addHandler(handler)



class ShippersAPI(Resource):
  def get(self):
    print("Entering get for ShippersAPI", sys.stdout)
    shippers = Shipper.objects().to_json()
    return Response(shippers, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json(force = True)
    shipper = Shipper(**body)
    shipper.save()
    # shipperIndex = 
    id = shipper.id
    return {'id': str(id)}, 200

class ShipperAPI(Resource):
  def get(self, id):
    shipper = Shipper.objects.get(id = id).to_json()
    return Response(shipper, mimetype="application/json", status=200)
  
  def put(self, id):
    shipper = Shipper.objects.get(id = id)
    body = request.get_json()
    Shipper.objects.get(id = id).update(**body)
    return '', 200
  
  def delete(self, id):
    shipper = Shipper.objects.get(id = id)
    shipper.delete()
    return '', 200

# class ShipperAPICompanyName(Resource):
#   def get(self, shipperCompanyName):
#     logger.info("Entering get of ShipperAPICompanyName")
#     shipper = Shipper.objects.get(shipperCompanyName = shipperCompanyName).to_json()
#     return Response(shipper, mimetype="application/json", status=200)   
