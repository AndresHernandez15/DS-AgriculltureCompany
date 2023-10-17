from datetime import datetime
from flask import render_template, request
from logic.crop import Crop
from logic.harvest import Harvest

class CropController:
    def __init__(self):
        self.model = []
        self.harvest_list = []

    """ Crop Methods """
    def crop(self):
        return render_template('crop.html')

    def crop_update(self, id_crop):
        return render_template('crop_update.html', id_crop=id_crop)

    def crop_detail(self):
        op = request.form['op']
        id_crop = int(request.form['id_crop'])
        crop_type = request.form['type']
        area = float(request.form['area'])
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        amount = int(request.form['amount'])
        price = float(request.form['price'])

        c = Crop(id_crop=id_crop, type=crop_type, area=area, date=date, amount=amount,
                 price=price)

        if op == 'I':
            self.model.append(c)
        elif op == 'U':
            for crop in self.model:
                if crop.id_crop == id_crop:
                    crop.type = crop_type
                    crop.area = area
                    crop.date = date
                    crop.amount = amount
                    crop.price = price
                    break

        return render_template('crop_detail.html', value=c)

    def cultivation(self):
        data = [(i.id_crop, i.type, i.area, i.date, i.amount, i.price) for i in self.model]
        return render_template('cultivation.html', value=data)

    def crop_delete(self, id_crop):
        self.model = [i for i in self.model if i.id_crop != int(id_crop)]
        data = [(i.id_crop, i.type, i.area, i.date, i.amount, i.price) for i in self.model]
        return render_template('cultivation.html', value=data)

    """ Harvest Methods """

    def harvest(self, id_harvest):
        return render_template('harvest.html', id_harvest=id_harvest)

    def harvest_update(self, id_harvest):
        return render_template('harvest_update.html', id_harvest=id_harvest)

    def harvest_detail(self):
        op = request.form['op']
        id_harvest = int(request.form['id_harvest'])
        crop_type = request.form['type']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        weight = float(request.form['weight'])

        h = Harvest(id_harvest=id_harvest, type=crop_type, date=date, weight=weight)
        print(h)
        if op == 'I':
            self.harvest_list.append(h)
        elif op == 'U':
            for row in self.harvest_list:
                if row.id_harvest == id_harvest:
                    row.type = crop_type
                    row.date = date
                    row.weight = weight
                    break

        self.model = [i for i in self.model if i.id_crop != int(id_harvest)]

        return render_template('harvest_detail.html', value=h)

    def harvested(self):
        data = [(i.id_harvest, i.type, i.date, i.weight) for i in self.harvest_list]
        return render_template('harvested.html', value=data)

    def harvest_delete(self, id_harvest):
        self.harvest_list = [i for i in self.harvest_list if i.id_harvest != int(id_harvest)]
        data = [(i.id_harvest, i.type, i.date, i.weight) for i in self.harvest_list]
        return render_template('harvested.html', value=data)
