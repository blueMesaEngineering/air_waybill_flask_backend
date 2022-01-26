


from .airWaybill import AirWaybillAPI, AirWaybillsAPI, AirWaybillAPICompanyName


def initialize_routes(api):
  api.add_resource(AirWaybillsAPI, '/api/airWaybills')
  api.add_resource(AirWaybillAPI, '/api/airWaybills/<id>')
  api.add_resource(AirWaybillAPICompanyName, '/api/airWaybills/companyName')