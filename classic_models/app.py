from flask import Flask
from classic_models.ext import configuration, commands
from classic_models.ext.database import db
import classic_models.blueprints

app = Flask(__name__)
configuration.init_app(app)
configuration.load_extensions(app)
db.init_app(app)
commands.init_app(app)


@app.route('/')
def index():
    return 'Hello World'
