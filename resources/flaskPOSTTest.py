from flask import Response, request 
import requests

url = "http://127.0.0.1:5000/api/airWaybillPDFCrossRefs"
crossRef = { "airWaybillSerialNumber": "1111000011110000", "airWaybillPDFID": "6398bf35b1f4e881633d5207"}
nextResponse = requests.post(url, json = crossRef)
print(nextResponse.text)