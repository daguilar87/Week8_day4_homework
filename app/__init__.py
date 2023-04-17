
from flask import Flask

from config import Config

from flask_cors import CORS

from .models import db, Product
from flask_migrate import Migrate

app = Flask(__name__)

cors = CORS(app, resources={r"/shop/<productid>*": {"origins": "*"}})
cors = CORS(app, resources={r"/shop*": {"origins": "*"}})


app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

from . import routes 