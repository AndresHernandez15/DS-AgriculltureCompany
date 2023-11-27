from datetime import datetime
from flask import render_template, request

from logic.crop import Crop
from logic.harvest import Harvest
from logic.silo import Silo
from logic.product import Product

class Controller:
    def __init__(self):
        self.crops = []
        self.harvests = []
        self.silos = []

    """ Crop Methods """

    def crop(self):
        return render_template('crop.html')

    def crop_update(self, id_crop):
        return render_template('crop_update.html', id_crop=id_crop)

    def crop_detail(self, op, id_crop, crop_type, area, date, amount, price):
        c = Crop(id_crop=id_crop, type=crop_type, area=area, date=date, amount=amount, price=price)

        if op == 'I':
            self.crops.append(c)
        elif op == 'U':
            for crop in self.crops:
                if crop.id_crop == id_crop:
                    crop.type = crop_type
                    crop.area = area
                    crop.date = date
                    crop.amount = amount
                    crop.price = price
                    break

        return render_template('crop_detail.html', value=c)

    def cultivation(self):
        data = [(i.id_crop, i.type, i.area, i.date, i.amount, i.price) for i in self.crops]
        return render_template('cultivation.html', value=data)

    def crop_delete(self, id_crop):
        self.crops = [i for i in self.crops if i.id_crop != id_crop]
        data = [(i.id_crop, i.type, i.area, i.date, i.amount, i.price) for i in self.crops]
        return render_template('cultivation.html', value=data)

    """ Harvest Methods """

    def harvest(self, id_harvest):
        return render_template('harvest.html', id_harvest=id_harvest)

    def harvest_update(self, id_harvest):
        return render_template('harvest_update.html', id_harvest=id_harvest)

    def harvest_detail(self, op, id_harvest, crop_type, date, weight):
        h = Harvest(id_harvest=id_harvest, type=crop_type, date=date, weight=weight)

        if op == 'I':
            self.harvests.append(h)
        elif op == 'U':
            for row in self.harvests:
                if row.id_harvest == id_harvest:
                    row.type = crop_type
                    row.date = date
                    row.weight = weight
                    break

        self.crops = [i for i in self.crops if i.id_crop != id_harvest]

        return render_template('harvest_detail.html', value=h)

    def harvested(self):
        data = [(i.id_harvest, i.type, i.date, i.weight) for i in self.harvests]
        return render_template('harvested.html', value=data)

    def harvest_delete(self, id_harvest):
        self.harvests = [i for i in self.harvests if i.id_harvest != id_harvest]
        data = [(i.id_harvest, i.type, i.date, i.weight) for i in self.harvests]
        return render_template('harvested.html', value=data)


    """ Silo Methods """


    def silo(self):
        return render_template('silo.html')

    def silo_update(self, id_silo):
        return render_template('silo_update.html', id_silo=id_silo)

    def silo_detail(self, op, capacity):
        if op == 'I':
            new_silo = Silo(capacity=capacity)
            self.silos.append(new_silo)
            s = new_silo
        elif op == 'U':
            id_silo = int(request.form['id_silo'])
            for silo in self.silos:
                if silo.id_silo == id_silo:
                    silo.capacity = capacity
                    s = silo
                    break

        return render_template('silo_detail.html', value=s)

    def silocreation(self):
        data = [(s.id_silo, s.capacity) for s in self.silos]
        return render_template('silocreation.html', value=data)

    def silo_delete(self, id_silo):
        self.silos = [s for s in self.silos if s.id_silo != id_silo]
        data = [(s.id_silo, s.capacity) for s in self.silos]
        return render_template('silocreation.html', value=data)

    """ Product Methods """

    def product(self, id_product):
        return render_template('product.html', id_product=id_product)

    def product_detail(self, op, silo, id_product, product_type, weight, sellprice, amount):
        p = Product(id_product=id_product, type=product_type, weight=weight, sellprice=sellprice, amount=amount)

        total_amount = 0
        for row in self.silos:
            for col in row.products:
                total_amount += col.amount

        if op == 'I':
            if self.silos[silo - 1].capacity >= total_amount:
                self.silos[silo - 1].products.append(p)
                # Eliminar el harvest correspondiente
                self.harvests = [harvest for harvest in self.harvests if harvest.id_harvest != id_product]
            else:
                return render_template('silofull.html')

        return render_template('product_detail.html', value=p, value2=silo)

    def products(self):
        data = []
        for row in self.silos:
            for col in row.products:
                data.append(col)
        return render_template('productcreation.html', value=data)

    def product_delete(self, id_product):
        data = []
        for row in self.silos:
            for col in row.products:
                if col.id_product == id_product:
                    row.products.remove(col)
                data.append(col)

        return render_template('productcreation.html', value=data)

    def show_products(self, id_silo):
        target_silo = None
        for silo in self.silos:
            if silo.id_silo == id_silo:
                target_silo = silo
                break

        if target_silo is not None:
            products = target_silo.products
            return render_template('show_product.html', value=products)
        else:
            return render_template('silo_not_found.html')
