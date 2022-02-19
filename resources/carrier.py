from flask import Response, request
from database.models import Carrier
from flask_restful import Resource
import logging
import sys


logger = logging.getLogger('werkzeug') 
handler = logging.FileHandler('test.log') 
logger.addHandler(handler)

class CarriersAPI(Resource):
  def get(self):
    print("Entering get for CarriersAPI", sys.stdout)
    carriers = Carrier.objects().to_json()
    return Response(carriers, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json(force = True)
    carrier = Carrier(**body)
    carrier.save()
    id = carrier.id
    return {'id': str(id)}, 200

class CarrierAPI(Resource):
  def get(self, id):
    carrier = Carrier.objects.get(id = id).to_json()
    return Response(carrier, mimetype="application/json", status=200)
  
  def put(self, id):
    carrier = Carrier.objects.get(id = id)
    body = request.get_json()
    Carrier.objects.get(id = id).update(**body)
    return '', 200
  
  def delete(self, id):
    carrier = Carrier.objects.get(id = id)
    carrier.delete()
    return '', 200

  # def getCompanyName(self, carrierCompanyName):
  #   carrier = Carrier.objects.get(carrierCompanyName = carrierCompanyName).to_json()
  #   return Response(carrier, mimetype="application/json", status=200)
  
class CarrierAPICompanyName(Resource):
  def get(self, carrierCompanyName):
    logger.info("Entering get of CarrierAPICompanyName")
    carrier = Carrier.objects.get(carrierFirstName = 'Nathan').to_json()
    return Response(carrier, mimetype="application/json", status=200)

    
    