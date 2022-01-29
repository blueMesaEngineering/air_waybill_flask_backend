


from .airWaybill import AirWaybillAPI, AirWaybillsAPI, AirWaybillAPICompanyName
from .shipper import ShipperAPI, ShippersAPI, ShipperAPICompanyName
from .consignee import ConsigneeAPI, ConsigneesAPI, ConsigneeAPICompanyName


def initialize_routes(api):
  api.add_resource(AirWaybillsAPI, '/api/airWaybills')
  api.add_resource(AirWaybillAPI, '/api/airWaybills/<id>')
  # api.add_resource(AirWaybillAPICompanyName, '/api/airWaybills/<companyName>')
  
  api.add_resource(ShippersAPI, '/api/shippers')
  api.add_resource(ShipperAPI, '/api/shippers/<id>')
  # api.add_resource(ShipperAPICompanyName, '/api/shippers/<companyName>')
  
  api.add_resource(ConsigneesAPI, '/api/airWaybills')
  api.add_resource(ConsigneeAPI, '/api/consignees/<id>')
  # api.add_resource(ConsigneeAPICompanyName, '/api/consignees/<companyName>')