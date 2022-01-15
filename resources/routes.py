


from .shipper import ShipperAPI, ShippersAPI, ShipperAPICompanyName


def initialize_routes(api):
  api.add_resource(ShippersAPI, '/api/shippers')
  api.add_resource(ShipperAPI, '/api/shippers/<id>')
  api.add_resource(ShipperAPICompanyName, '/api/shippers/companyName')