from flask import request
from flask_restful import Resource
from classic_models.ext.database import db
from classic_models.models import Customers, Employees, Offices


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
