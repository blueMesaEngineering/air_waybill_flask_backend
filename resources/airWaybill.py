from flask import Response, request 
import requests
from database.models import AirWaybill
from flask_restful import Resource
import sys

class AirWaybillsAPI(Resource):
  def get(self):
    print("Entering get for AirWaybillsAPI", sys.stdout)
    airWaybills = AirWaybill.objects().to_json()
    print("Leaving get for AirWaybillsAPI", sys.stdout)
    return Response(airWaybills, mimetype="application/json", status=200)

  def post(self):
    print("Entering POST for AirWaybillsAPI", sys.stdout)
    body = request.get_json(force = True)
    print("request.get_json(force = True) succeeded", sys.stdout)
    airWaybill = AirWaybill(**body)
    print("AirWaybill(**body) succeeded", sys.stdout)
    print(airWaybill.to_json(), sys.stdout)
    airWaybill.save()
    print("airWaybill.save() succeeded", sys.stdout)
    id = airWaybill.id
    print("airWaybill.id succeeded", sys.stdout)
    url = "http://127.0.0.1:5000/api/airWaybillPDFCrossRef"
    crossRef = { "airWaybillSerialNumber": str(id), "airWaybillPDFID": body['serialNumberAWBPDF'].strip()}
    nextResponse = requests.post(url, json = crossRef)
    print(nextResponse.text)
    # <-- The code commands to insert the corresponding PDF into the PDF collection should probably go here. NDG 20221213:1948
    print("Leaving POST for AirWaybillsAPI", sys.stdout)
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
    
    