from flask import Response, request, requests
from database.models import AirWaybill
from flask_restful import Resource
import sys

class AirWaybillsAPI(Resource):
  def get(self):
    print("Entering get for AirWaybillsAPI", sys.stdout)
    airWaybills = AirWaybill.objects().to_json()
    return Response(airWaybills, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json(force = True)
    airWaybill = AirWaybill(**body)
    airWaybill.save()
    id = airWaybill.id
    url = "http://127.0.0.1:5000/api/airWaybills"
    crossRef = {id, body['serialNumberAWBPDF'].strip()}
    nextResponse = requests.post(url, json = crossRef)
    print(nextResponse.text)
    # <-- The code commands to insert the corresponding PDF into the PDF collection should probably go here. NDG 20221213:1948
    return {'id': str(id)}, 200

class AirWaybillAPI(Resource):
  def get(self, id):
    airWaybill = AirWaybill.objects.get(id = id).to_json()
    return Response(airWaybill, mimetype="application/json", status=200)
  
  def put(self, id):
    airWaybill = AirWaybill.objects.get(id = id)
    body = request.get_json()
    AirWaybill.objects.get(id = id).update(**body)
    return '', 200
  
  def delete(self, id):
    airWaybill = AirWaybill.objects.get(id = id)
    airWaybill.delete()
    return '', 200
    
    