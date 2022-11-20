from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from database.db import initialize_db
from resources.routes import initialize_routes
from flask_restful import Api
from flask_marshmallow import Marshmallow
import logging

app = Flask(__name__)
ma = Marshmallow(app)

logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('test.log')
logger.addHandler(handler)
# logging.getLogger('flask_cors').level = logging.DEBUG
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# cors = CORS(app)
CORS(app)
app.config.from_envvar('ENV_FILE_LOCATION')
app.config['PROPAGATE_EXCEPTIONS']  # https://stackoverflow.com/questions/54648603/how-should-i-handle-exceptions-raised-in-jwt-required-decorator-in-flask-jwt
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
  'host': 'mongodb://localhost/air_waybill_flask_backend'
}

initialize_db(app)
initialize_routes(api)


class ShipperSchema(ma.Schema):
  class Meta:
    fields = ("shipperFirstName", "shipperMiddleName", "shipperLastName", "shipperCompanyName", "shipperStreetAddress1", "shipperStreetAddress2", "shipperCity", "shipperStateUSA")
    
  _links = ma.Hyperlinks(
    {
      "self": ma.URLFor("shipper_detail", values=dict(id="<id>")),
      "collection": ma.URLFor("shippers")
    }
  )

shipper_schema = ShipperSchema()
shippers_schema = ShipperSchema(many = True)

if __name__ == "__main__":
  app.run()