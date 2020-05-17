from classic_models.ext.database import db


class Customers(db.Model):
    __tablename__ = 'customers'
    customerNumber = db.Column(db.Integer, primary_key=True)
    customerName = db.Column(db.String(50))
    contactLastName = db.Column(db.String(30))
    contactFirstName = db.Column(db.String(30))
    phone = db.Column(db.String(15))
    addressLine1 = db.Column(db.String(40))
    addressLine2 = db.Column(db.String(40))
    city = db.Column(db.String(25))
    state = db.Column(db.String(25))
    postalCode = db.Column(db.String(10))
    country = db.Column(db.String(25))
    salesRepEmployeeNumber = db.Column(db.Integer, db.ForeignKey('employees.employeeNumber'))
    creditLimit = db.Column(db.Integer)

    employees = db.relationship('Employees')

    def __repr__(self):
        return '<Customer Name {}>'.format(self.customerName)


class Employees(db.Model):
    __tablename__ = 'employees'
    employeeNumber = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(20))
    firstName = db.Column(db.String(20))
    extension = db.Column(db.String(10))
    email = db.Column(db.String(50))
    officeCode = db.Column(db.String(5), db.ForeignKey('offices.officeCode'))
    reportsTo = db.Column(db.Integer, db.ForeignKey('employees.employeeNumber'))
    jobTitle = db.Column(db.String(15))

    offices = db.relationship('Offices')
    employees = db.relationship('Employees')

    def __repr__(self):
        return '<Name: {} {}>'.format(self.lastName, self.firstName)


class Offices(db.Model):
    __tablename__ = 'offices'
    officeCode = db.Column(db.String(5), primary_key=True)
    city = db.Column(db.String(15))
    phone = db.Column(db.String(20))
    addressLine1 = db.Column(db.String(40))
    addressLine2 = db.Column(db.String(40))
    state = db.Column(db.String(20))
    country = db.Column(db.String(20))
    postalCode = db.Column(db.String(15))
    territory = db.Column(db.String(15))

    def __repr__(self):
        return '<Office: {}>'.format(self.officeCode)


class OrderDetails(db.Model):
    __tablename__ = 'orderDetails'
    orderNumber = db.Column(db.Integer, db.ForeignKey('orders.orderNumber'), primary_key=True)
    productCode = db.Column(db.String(20), db.ForeignKey('products.productCode'), primary_key=True)
    quantityOrdered = db.Column(db.Integer)
    priceEach = db.Column(db.Float)
    orderLineNumber = db.Column(db.Integer)

    orders = db.relationship('Orders')
    products = db.relationship('Products')

    def __repr__(self):
        return '<Order Number: {}>'.format(self.orderNumber)


class Orders(db.Model):
    __tablename__ = 'orders'
    orderNumber = db.Column(db.Integer, primary_key=True)
    orderDate = db.Column(db.Date)
    requiredDate = db.Column(db.Date)
    shippedDate = db.Column(db.Date)
    status = db.Column(db.String(10))
    comments = db.Column(db.String(100))
    customerNumber = db.Column(db.Integer, db.ForeignKey('customers.customerNumber'))

    customers = db.relationship('Customers')

    def __repr__(self):
        return '<Order Number: {}>'.format(self.orderNumber)


class Payments(db.Model):
    __tablename__ = 'payments'
    customerNumber = db.Column(db.Integer, db.ForeignKey('customers.customerNumber'))
    checkNumber = db.Column(db.String(15), primary_key=True)
    paymentDate = db.Column(db.Date)
    amount = db.Column(db.Float)

    customers = db.relationship('Customers')

    def __repr__(self):
        return '<Check Number: {}>'.format(self.checkNumber)


class ProductLines(db.Model):
    __tablename__ = 'productLines'
    productLine = db.Column(db.String(50), primary_key=True)
    textDescription = db.Column(db.String())
    htmlDescription = db.Column(db.String())
    image = db.Column(db.String())

    def __repr__(self):
        return '<Product Line: {}>'.format(self.productLine)


class Products(db.Model):
    __tablename__ = 'products'
    productCode = db.Column(db.String(20), primary_key=True)
    productName = db.Column(db.String(50))
    productLine = db.Column(db.String(), db.ForeignKey('productLines.productLine'))
    productScale = db.Column(db.String(30))
    productVendor = db.Column(db.String(30))
    productDescription = db.Column(db.String(250))
    quantityInStock = db.Column(db.Integer)
    buyPrice = db.Column(db.Float)
    MSRP = db.Column(db.Float)

    productLines = db.relationship('ProductLines')
