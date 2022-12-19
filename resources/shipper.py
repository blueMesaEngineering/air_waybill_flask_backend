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
    print("Entering GET for ShippersAPI", sys.stdout)
    shippers = Shipper.objects().to_json()
    print("Leaving GET for ShippersAPI", sys.stdout)
    return Response(shippers, mimetype="application/json", status=200)

  def post(self):
    print("Entering POST for ShippersAPI", sys.stdout)
    body = request.get_json(force = True)
    shipper = Shipper(**body)
    print("Shipper(**body) succeeded", sys.stdout)
    print(shipper.to_json(), sys.stdout)
    shipper.save()
    print("shipper.save() succeeded", sys.stdout)
    # shipperIndex = 
    id = shipper.id
    print("Leaving POST for ShippersAPI", sys.stdout)
    return {'id': str(id)}, 200

class ShipperAPI(Resource):
  def get(self, id):
    print("Entering GET for ShipperAPI", sys.stdout)
    shipper = Shipper.objects.get(id = id).to_json()
    print("Leaving GET for ShippersAPI", sys.stdout)
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
