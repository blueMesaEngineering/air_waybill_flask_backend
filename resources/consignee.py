from flask import Response, request
from database.models import Consignee
from flask_restful import Resource
import sys

class ConsigneesAPI(Resource):
  def get(self):
    print("Entering get for ConsigneesAPI", sys.stdout)
    consignees = Consignee.objects().to_json()
    return Response(consignees, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json(force = True)
    consignee = Consignee(**body)
    consignee.save()
    id = consignee.id
    return {'id': str(id)}, 200

class ConsigneeAPI(Resource):
  def get(self, id):
    consignee = Consignee.objects.get(id = id).to_json()
    return Response(consignee, mimetype="application/json", status=200)
  
  def put(self, id):
    consignee = Consignee.objects.get(id = id)
    body = request.get_json()
    Consignee.objects.get(id = id).update(**body)
    return '', 200
  
  def delete(self, id):
    consignee = Consignee.objects.get(id = id)
    consignee.delete()
    return '', 200

#   def getCompanyName(self, companyName):
#     consignee = Consignee.objects.get(companyName = companyName).to_json()
#     return Response(consignee, mimetype="application/json", status=200)
  
# class ConsigneeAPICompanyName(Resource):
#   def get(self, companyname):
#     consignee = Consignee.objects.get(companyname = companyname)
#     return Response(consignee, mimetype="application/json", status=200)

    
    