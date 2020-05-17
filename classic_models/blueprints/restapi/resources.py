from flask import request
from flask_restful import Resource
from datetime import datetime
import urllib.parse
from classic_models.ext.database import db
from classic_models.models import Customers, Employees, Offices, OrderDetails, Orders, Payments
from classic_models.models import Products, ProductLines

class Customer(Resource):
    def get(self, id):
        data = Customers.query.filter_by(customerNumber=id).first()
        customer = {
            "customerNumber": data.customerNumber,
            "customerName": data.customerName,
            "contactLastName": data.contactLastName,
            "contactFirstName": data.contactFirstName,
            "phone": data.phone,
            "addressLine1": data.addressLine1,
            "addressLine2": data.addressLine2,
            "city": data.city,
            "state": data.state,
            "postalCode": data.postalCode,
            "country": data.country,
            "salesRepEmployeeNumber": data.salesRepEmployeeNumber,
            "creditLimit": data.creditLimit
        }
        return customer


class CustomersList(Resource):
    def get(self):
        data = Customers.query.all()
        customers = []
        for customer in data:
            customers.append({
                "customerNumber": customer.customerNumber,
                "customerName": customer.customerName,
                "contactLastName": customer.contactLastName,
                "contactFirstName": customer.contactFirstName,
                "phone": customer.phone,
                "addressLine1": customer.addressLine1,
                "addressLine2": customer.addressLine2,
                "city": customer.city,
                "state": customer.state,
                "postalCode": customer.postalCode,
                "country": customer.country,
                "salesRepEmployeeNumber": customer.salesRepEmployeeNumber,
                "creditLimit": customer.creditLimit
            })
        return customers

    def post(self):
        data = request.json
        if type(data) == list:
            for customer in data:
                customers = Customers(
                    customerNumber=customer['customerNumber'],
                    customerName=customer['customerName'],
                    contactLastName=customer['contactLastName'],
                    contactFirstName=customer['contactFirstName'],
                    phone=customer['phone'],
                    addressLine1=customer['addressLine1'],
                    addressLine2=customer['addressLine2'],
                    city=customer['city'],
                    state=customer['state'],
                    postalCode=customer['postalCode'],
                    country=customer['country'],
                    salesRepEmployeeNumber=customer['salesRepEmployeeNumber'],
                    creditLimit=customer['creditLimit']
                )
                db.session.add(customers)
                db.session.commit()
        else:
            customers = Customers(
                customerNumber=data['customerNumber'],
                customerName=data['customerName'],
                contactLastName=data['contactLastName'],
                contactFirstName=data['contactFirstName'],
                phone=data['phone'],
                addressLine1=data['addressLine1'],
                addressLine2=data['adressLine2'],
                city=data['city'],
                state=data['state'],
                postalCode=data['postalCode'],
                country=data['country'],
                salesRepEmployeeNumber=data['salesRepEmployeeNumber'],
                creditLimit=data['creditLimit']
            )
        return {"Status": "Successfully Created!"}


class Employee(Resource):
    def get(self, id):
        emp = Employees.query.filter_by(employeeNumber=id).first()
        employee = {
            "employeeNumber": emp.employeeNumber,
            "lastName": emp.lastName,
            "firstName": emp.firstName,
            "extension": emp.extension,
            "email": emp.email,
            "officeCode": emp.officeCode,
            "reportsTo": emp.reportsTo,
            "jobTitle": emp.jobTitle
        }
        return employee

class EmployeesList(Resource):
    def get(self):
        data = Employees.query.all()
        employees = []
        for emp in data:
            employees.append({
                "employeeNumber": emp.employeeNumber,
                "lastName": emp.lastName,
                "firstName": emp.firstName,
                "extension": emp.extension,
                "email": emp.email,
                "officeCode": emp.officeCode,
                "reportsTo": emp.reportsTo,
                "jobTitle": emp.jobTitle
            })
        return employees

    def post(self):
        data = request.json
        if type(data) == list:
            for emp in data:
                employee = Employees(
                    employeeNumber=emp['employeeNumber'],
                    lastName=emp['lastName'],
                    firstName=emp['firstName'],
                    extension=emp['extension'],
                    email=emp['email'],
                    officeCode=emp['officeCode'],
                    reportsTo=emp['reportsTo'],
                    jobTitle=emp['jobTitle']
                )

                db.session.add(employee)
                db.session.commit()
            return {"Status": "Successfully Created!"}
        else:
            employee = Employees(
                employeeNumber=data['employeeNumber'],
                lastName=data['lastName'],
                firstName=data['firstName'],
                extension=data['extension'],
                email=data['email'],
                officeCode=data['officeCode'],
                reportsTo=data['reportsTo'],
                jobTitle=data['jobTitle']
            )
            return {"Status": "Successfully Created!"}


class Office(Resource):
    def get(self, id):
        off = Offices.query.filter_by(officeCode=id).first()
        office = {
            "officeCode": off.officeCode,
            "city": off.city,
            "phone": off.phone,
            "addressLine1": off.addressLine1,
            "addressLine2": off.addressLine2,
            "state": off.state,
            "country": off.country,
            "postalCode": off.postalCode,
            "territory": off.territory
        }
        return office

class OfficesList(Resource):
    def get(self):
        data = Offices.query.all()
        offices = []
        for off in data:
            offices.append({
                "officeCode": off.officeCode,
                "city": off.city,
                "phone": off.phone,
                "addressLine1": off.addressLine1,
                "addressLine2": off.addressLine2,
                "state": off.state,
                "country": off.country,
                "postalCode": off.postalCode,
                "territory": off.territory
            })
        return offices

    def post(self):
        data = request.json
        if type(data) == list:
            for off in data:
                offices = Offices(
                    officeCode=off['officeCode'],
                    city=off['city'],
                    phone=off['phone'],
                    addressLine1=off['addressLine1'],
                    addressLine2=off['addressLine2'],
                    state=off['state'],
                    country=off['country'],
                    postalCode=off['postalCode'],
                    territory=off['territory']
                )
                db.session.add(offices)
                db.session.commit()
            return {"Status": "Successfully Created!"}
        else:
            offices = Offices(
                officeCode=data['officeCode'],
                city=data['city'],
                phone=data['phone'],
                addressLine1=data['addressLine1'],
                addressLine2=data['addressLine2'],
                state=data['state'],
                country=data['country'],
                postalCode=data['postalCode'],
                territory=data['territory']
            )
            db.session.add(offices)
            db.session.commit()
            return {"Status": "Successfully Created!"}


class OrderDetail(Resource):
    def get(self, id, pc):
        data = OrderDetails.query.filter_by(orderNumber=id, productCode=pc.upper()).first()
        orderDetail = {
            "orderNumber": data.orderNumber,
            "productCode": data.productCode,
            "quantityOrdered": data.quantityOrdered,
            "priceEach": data.priceEach,
            "orderLineNumber": data.orderLineNumber
        }
        return orderDetail

class OrderDetailsList(Resource):
    def get(self):
        data = OrderDetails.query.all()
        orderDetails = []
        for orderDetail in data:
            orderDetails.append({
                "orderNumber": orderDetail.orderNumber,
                "productCode": orderDetail.productCode,
                "quantityOrdered": orderDetail.quantityOrdered,
                "priceEach": orderDetail.priceEach,
                "orderLineNumber": orderDetail.orderLineNumber
            })
        return orderDetails

    def post(self):
        data = request.json
        if type(data) == list:
            for od in data:
                orderDetails = OrderDetails(
                    orderNumber=od['orderNumber'],
                    productCode=od['productCode'],
                    quantityOrdered=od['quantityOrdered'],
                    priceEach=od['priceEach'],
                    orderLineNumber=od['orderLineNumber']
                )
                db.session.add(orderDetails)
                db.session.commit()
            return {"Status": "Successfully Created!"}
        else:
            orderDetails = OrderDetails(
                orderNumber=data['orderNumber'],
                productCode=data['productCode'],
                quantityOrdered=data['quantityOrdered'],
                priceEach=data['priceEach'],
                orderLineNumber=data['orderLineNumber']
            )
            db.session.add(orderDetails)
            db.session.commit()
            return {"Status": "Successfully Created!"}


class Order(Resource):
    def get(self, id):
        data = Orders.query.filter_by(orderNumber=id).first()
        order = {
            "orderNumber": data.orderNumber,
            "orderDate": str(data.orderDate),
            "requiredDate": str(data.requiredDate),
            "shippedDate": str(data.shippedDate),
            "status": data.status,
            "comments": data.comments,
            "customerNumber": data.customerNumber
        }
        return order

class OrdersList(Resource):
    def get(self):
        data = Orders.query.all()
        orders = []
        for od in data:
            orders.append({
                "orderNumber": od.orderNumber,
                "orderDate": str(od.orderDate),
                "requiredDate": str(od.requiredDate),
                "shippedDate": str(od.shippedDate) if od.shippedDate is not None else None,
                "status": od.status,
                "comments": od.comments,
                "customerNumber": od.customerNumber
            })
        return orders

    def post(self):
        data = request.json
        if type(data) == list:
            for od in data:
                order = Orders(
                    orderNumber=od['orderNumber'],
                    orderDate=datetime.strptime(od['orderDate'], '%Y-%m-%d').date(),
                    requiredDate=datetime.strptime(od['requiredDate'], '%Y-%m-%d').date(),
                    shippedDate=datetime.strptime(od['shippedDate'], '%Y-%m-%d').date() if od['shippedDate'] is not None else None,
                    status=od['status'],
                    comments=od['comments'],
                    customerNumber=od['customerNumber']
                )
                db.session.add(order)
                db.session.commit()
            return {"Status": "Successfully Created!"}
        else:
            orders = Orders(
                orderNumber=data['orderNumber'],
                orderDate=datetime.strptime(data['orderDate'], '%Y-%m-%d').date(),
                requiredDate=datetime.strptime(data['requiredDate'], '%Y-%m-%d').date(),
                shippedDate=datetime.strptime(data['shippedDate'], '%Y-%m-%d').date() if data['shippedDate'] is not None else None,
                status=data['status'],
                comments=data['comments'],
                customerNumber=data['customerNumber']
            )
            db.session.add(orders)
            db.session.commit()
            return {"Status": "Successfuly Created!"}


class Payment(Resource):
    def get(self, ckn):
        data = Payments.query.filter_by(checkNumber=ckn.upper()).first()
        payment = {
            "customerNumber": data.customerNumber,
            "checkNumber": data.checkNumber,
            "paymentDate": str(data.paymentDate),
            "amount": data.amount
        }
        return payment

class PaymentsList(Resource):
    def get(self):
        data = Payments.query.all()
        payments = []
        for pay in data:
            payments.append({
                "customerNumber": pay.customerNumber,
                "checkNumber": pay.checkNumber,
                "paymentDate": str(pay.paymentDate),
                "amount": pay.amount
            })
        return payments

    def post(self):
        data = request.json
        if type(data) == list:
            for pay in data:
                payment = Payments(
                    customerNumber=pay['customerNumber'],
                    checkNumber=pay['checkNumber'],
                    paymentDate=datetime.strptime(pay['paymentDate'], '%Y-%m-%d').date(),
                    amount=pay['amount']
                )
                db.session.add(payment)
                db.session.commit()
            return {"Status": "Successfuly Created!"}
        else:
            payment = Payments(
                customerNumber=data['customerNumber'],
                checkNumber=data['checkNumber'],
                paymentDate=datetime.strptime(data['paymentDate'], '%Y-%m-%d').date(),
                amount=data['amount']
            )
            db.session.add(payment)
            db.session.commit()
            return {"Status": "Successfuly Created!"}


class Product(Resource):
    def get(self, pc):
        data = Products.query.filter_by(productCode=pc.upper()).first()
        product = {
            "productCode": data.productCode,
            "productName": data.productName,
            "productLine": data.productLine,
            "productScale": data.productScale,
            "productVendor": data.productVendor,
            "productDescription": data.productDescription,
            "quantityInStock": data.quantityInStock,
            "buyPrice": data.buyPrice,
            "MSRP": data.MSRP
        }
        return product


class ProductsList(Resource):
    def get(self):
        data = Products.query.all()
        products = []
        for prod in data:
            products.append({
                "productCode": prod.productCode,
                "productName": prod.productName,
                "productLine": prod.productLine,
                "productScale": prod.productScale,
                "productVendor": prod.productVendor,
                "productDescription": prod.productDescription,
                "quantityInStock": prod.quantityInStock,
                "buyPrice": prod.buyPrice,
                "MSRP": prod.MSRP
            })
        return products

    def post(self):
        data = request.json
        if type(data) == list:
            for prod in data:
                product = Products(
                    productCode=prod['productCode'],
                    productName=prod['productName'],
                    productLine=prod['productLine'],
                    productScale=prod['productScale'],
                    productVendor=prod['productVendor'],
                    productDescription=prod['productDescription'],
                    quantityInStock=prod['quantityInStock'],
                    buyPrice=prod['buyPrice'],
                    MSRP=prod['MSRP']
                )
                db.session.add(product)
                db.session.commit()
            return {"Status": "Successfully Created!"}
        else:
            prod = Products(
                productCode=data['productCode'],
                productName=data['productName'],
                productLine=data['productLine'],
                productScale=data['productScale'],
                productVendor=data['productVendor'],
                productDescription=data['productDescription'],
                quantityInStock=data['quantityInStock'],
                buyPrice=data['buyPrice'],
                MSRP=data['MSRP']
            )
            db.session.add(product)
            db.session.commit()
            return {"Status": "Successfully Created!"}


class ProductLine(Resource):
    def get(self, pl):
        pl = urllib.parse.unquote_plus(pl)
        data = ProductLines.query.filter_by(productLine=pl).first()
        productLine = {
            "productLine": data.productLine,
            "textDescription": data.textDescription,
            "htmlDescription": data.htmlDescription,
            "image": data.image
        }
        return productLine

class ProductLinesList(Resource):
    def get(self):
        data = ProductLines.query.all()
        productLines = []
        for prod in data:
            productLines.append({
                "productLine": prod.productLine,
                "textDescription": prod.textDescription,
                "htmlDescription": prod.htmlDescription,
                "image": prod.image
            })
        return productLines

    def post(self):
        data = request.json
        if type(data) == list:
            for prod in data:
                productLine = ProductLines(
                    productLine=prod['productLine'],
                    textDescription=prod['textDescription'],
                    htmlDescription=prod['htmlDescription'],
                    image=prod['image']
                )
                db.session.add(productLine)
                db.session.commit()
            return {"Status": "Successfully Created!"}
        else:
            productLine = ProductLines(
                productLine=data['productLine'],
                textDescription=data['textDescription'],
                htmlDescription=data['htmlDescription'],
                image=data['image']
            )
            db.session.add(productLine)
            db.session.commit()
            return {"Status": "Successfully Created!"}
