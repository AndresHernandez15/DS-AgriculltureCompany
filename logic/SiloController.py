from flask import render_template, request
from logic.silo import Silo
from logic.product import Product


class SiloController:
    def __init__(self):
        self.model = []

    def silo(self):
        return render_template('silo.html')

    def silo_update(self, id_silo):
        return render_template('silo_update.html', id_silo=id_silo)

    def silocreation(self):
        data = [(i.id_silo, i.capacity) for i in self.model]
        return render_template('silocreation.html', value=data)

    def silo_detail(self):
        op = request.form['op']
        id_silo = int(request.form['id_silo'])
        capacity = int(request.form['capacity'])

        s = Silo(id_silo=id_silo, capacity=capacity)
        print(s)
        if op == 'I':
            self.model.append(s)
        elif op == 'U':
            for silo in self.model:
                if silo.id_silo == id_silo:
                    silo.capacity = capacity
                    break

        return render_template('silo_detail.html', value=s)

    def silo_delete(self, id_silo):
        self.model = [i for i in self.model if i.id_silo != int(id_silo)]
        data = [(i.id_silo, i.capacity) for i in self.model]
        return render_template('silocreation.html', value=data)

    def product(self, id_product):
        return render_template('product.html', id_product=id_product)

    def product_update(self, id_product):
        return render_template('product_update.html', id_product=id_product)

    def product_detail(self):
        op = request.form['op']
        id_product = int(request.form['id_product'])
        product_type = request.form['type']
        weight = float(request.form['weight'])
        sellprice = float(request.form['sellprice'])

        p = Product(id_product=id_product, type=product_type, weight=weight, sellprice=sellprice)
        print(p)
        if op == 'I':
            self.model.append(p)
        elif op == 'U':
            for row in self.model:
                if row.id_product == id_product:
                    row.type = product_type
                    row.weight = weight
                    row.sellprice = sellprice
                    break

        self.model = [i for i in self.model if i.id_product != int(id_product)]

        return render_template('product_detail.html', value=p)

    def products(self):
        data = [(i.id_product, i.type, i.date, i.weight) for i in self.model]
        return render_template('productcreation.html', value=data)

    def product_delete(self, id_product):
        self.model = [i for i in self.model if i.id_product != int(id_product)]
        data = [(i.id_product, i.type, i.weight, i.sellprice) for i in self.model]
        return render_template('productcreation.html', value=data)
