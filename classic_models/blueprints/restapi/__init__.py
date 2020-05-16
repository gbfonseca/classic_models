from flask import Blueprint
from flask_restful import Api

from .resources import Customer, CustomersList, Employee, EmployeesList, Office, OfficesList

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")

api = Api(bp)

def init_app(app):
    api.add_resource(CustomersList, "/customers/")
    api.add_resource(Customer, "/customers/<int:id>")
    api.add_resource(EmployeesList, "/employees/")
    api.add_resource(Employee, "/employees/<int:id>")
    api.add_resource(OfficesList, "/offices/")
    api.add_resource(Office, "/offices/<int:id>")
    app.register_blueprint(bp)
