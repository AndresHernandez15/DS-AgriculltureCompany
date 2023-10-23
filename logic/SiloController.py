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
        silo = int(request.form['silo'])
        id_product = int(request.form['id_product'])
        product_type = request.form['type']
        weight = float(request.form['weight'])
        sellprice = float(request.form['sellprice'])
        amount = int(request.form['amount'])

        p = Product(id_product=id_product, type=product_type, weight=weight, sellprice=sellprice, amount=amount)
        print(p)
        total_amount = 0
        for row in self.model:
            for col in row.products:
                total_amount += col.amount

        if op == 'I':
            if self.model[silo-1].capacity >= total_amount:
                self.model[silo-1].products.append(p)
            else:
                return render_template('silofull.html')
        elif op == 'U':
            for row in self.model:
                for col in row.products:
                    if col.id_product == id_product:
                        if row.id_silo == silo:
                            col.type = product_type
                            col.weight = weight
                            col.sellprice = sellprice
                            break
                        else:
                            if self.model[silo - 1].capacity <= total_amount:
                                self.model[silo - 1].products(p)
                            row.products.remove(col)

        return render_template('product_detail.html', value=p, value2=silo)

    def products(self):
        data = []
        for row in self.model:
            for col in row.products:
                data.append(col)
        print(data)
        return render_template('productcreation.html', value=data)

    def product_delete(self, id_product):
        data = []
        for row in self.model:
            for col in row.products:
                if col.id_product == id_product:
                    row.products.remove(col)
                data.append(col)

        return render_template('productcreation.html', value=data)

    def show_products(self, id_silo):
        products = []
        for row in self.model:
            for col in row.products:
                products.append(col)
        return render_template('show_product.html', value=products)
