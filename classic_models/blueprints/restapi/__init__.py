from flask import Blueprint
from flask_restful import Api
from .resources import Customer, CustomersList, Employee, EmployeesList, Office, OfficesList
from .resources import Order, OrdersList, OrderDetail, OrderDetailsList, Payment, PaymentsList
from .resources import Product, ProductsList, ProductLine, ProductLinesList
bp = Blueprint("restapi", __name__, url_prefix="/api/v1")

api = Api(bp)

def init_app(app):
    api.add_resource(CustomersList, "/customers/")
    api.add_resource(Customer, "/customers/<int:id>")
    api.add_resource(EmployeesList, "/employees/")
    api.add_resource(Employee, "/employees/<int:id>")
    api.add_resource(OfficesList, "/offices/")
    api.add_resource(Office, "/offices/<int:id>")
    api.add_resource(OrdersList, "/orders/")
    api.add_resource(Order, "/orders/<int:id>/")
    api.add_resource(OrderDetailsList, "/orderdetails/")
    api.add_resource(OrderDetail, "/orderdetails/<int:id>/<string:pc>/")
    api.add_resource(PaymentsList, "/payments/")
    api.add_resource(Payment, "/payments/<string:ckn>")
    api.add_resource(ProductsList, "/products/")
    api.add_resource(Product, "/products/<string:pc>/")
    api.add_resource(ProductLinesList, "/productlines/")
    api.add_resource(ProductLine, "/productlines/<string:pl>/")
    app.register_blueprint(bp)
