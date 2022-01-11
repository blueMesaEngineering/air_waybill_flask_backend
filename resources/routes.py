


from .shipper import ShipperAPI, ShippersAPI


def initialize_routes(api):
  api.add_resource(ShippersAPI, '/api/shippers')
  api.add_resource(ShipperAPI, '/api/shippers/<id>')