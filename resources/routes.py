
from .airWaybill import AirWaybillAPI, AirWaybillsAPI
from .shipper import ShipperAPI, ShippersAPI
from .consignee import ConsigneeAPI, ConsigneesAPI
from .carrier import CarrierAPI, CarriersAPI


def initialize_routes(api):
  api.add_resource(AirWaybillsAPI, '/api/airWaybills')
  api.add_resource(AirWaybillAPI, '/api/airWaybills/<id>')
  # api.add_resource(AirWaybillAPICompanyName, '/api/airWaybills/<companyName>')
  
  api.add_resource(ShippersAPI, '/api/shippers')
  api.add_resource(ShipperAPI, '/api/shippers/<id>')
  # api.add_resource(ShipperAPICompanyName, '/api/shippers/<shipperCompanyName>')
  
  api.add_resource(ConsigneesAPI, '/api/consignees')
  api.add_resource(ConsigneeAPI, '/api/consignees/<id>')
  # api.add_resource(ConsigneeAPICompanyName, '/api/consignees/<companyName>')
  
  api.add_resource(CarriersAPI, '/api/carriers')
  api.add_resource(CarrierAPI, '/api/carriers/<id>')
  # api.add_resource(CarrierAPICompanyName, '/api/carriers/<companyName>')