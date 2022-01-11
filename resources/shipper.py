from flask import Response, request
from database.models import Shipper
from flask_restful import Resource

class ShippersAPI(Resource):
  def get(self):
    shippers = Shipper.objects().to_json()
    return Response(shippers, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json(force = True)
    shipper = Shipper(**body)
    shipper.save()
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