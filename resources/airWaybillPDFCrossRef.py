from flask import Response, request
from database.models import AirWaybillPDFCrossRef
from flask_restful import Resource
import logging
import sys


logger = logging.getLogger('werkzeug') 
handler = logging.FileHandler('test.log') 
logger.addHandler(handler)

class AirWaybillPDFCrossRefsAPI(Resource):
  def get(self):
    print("Entering get for AirWaybillPDFCrossRefsAPI", sys.stdout)
    airWaybillPDFCrossRefs = AirWaybillPDFCrossRef.objects().to_json()
    return Response(airWaybillPDFCrossRefs, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json(force = True)
    airWaybillPDFCrossRef = AirWaybillPDFCrossRef(**body)
    airWaybillPDFCrossRef.save()
    id = airWaybillPDFCrossRef.id
    return {'id': str(id)}, 200

class AirWaybillPDFCrossRefAPI(Resource):
  def get(self, id):
    airWaybillPDFCrossRef = AirWaybillPDFCrossRef.objects.get(id = id).to_json()
    return Response(airWaybillPDFCrossRef, mimetype="application/json", status=200)
  
  def put(self, id):
    airWaybillPDFCrossRef = AirWaybillPDFCrossRef.objects.get(id = id)
    body = request.get_json()
    AirWaybillPDFCrossRef.objects.get(id = id).update(**body)
    return '', 200
  
  def delete(self, id):
    airWaybillPDFCrossRef = AirWaybillPDFCrossRef.objects.get(id = id)
    airWaybillPDFCrossRef.delete()
    return '', 200
