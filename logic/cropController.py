from flask import render_template, request
from logic.crop import Crop
from logic.harvest import Harvest
from datetime import datetime


class CropController:
    def __init__(self):
        self.model = []

    def crop(self):
        return render_template('crop.html')

    def crop_detail(self):
        op = request.form['op']
        crop_type = request.form['crop_type']
        area = float(request.form['area'])
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        amount = int(request.form['amount'])
        expenses = float(request.form['expenses'])

        c = Crop(type=crop_type, area=area, date=date, amount=amount, price=expenses)

        if op == 'I':
            self.model.append(c)
        elif op == 'U':
            for crop in self.model:
                if crop.id_crop == c.id_crop:
                    crop.type = crop_type
                    crop.area = area
                    crop.date = date
                    crop.amount = amount
                    crop.price = expenses
                    break

        return render_template('crop_detail.html', value=c)

    def cultivation(self):
        data = [(i.id_crop, i.type, i.area, i.date, i.amount, i.price) for i in self.model]
        return render_template('cultivation.html', value=data)

    def crop_update(self, id_crop):
        return render_template('crop_update.html', id_crop=id_crop)

    def crop_delete(self, id_crop):
        self.model = [i for i in self.model if i.id_crop != id_crop]
        data = [(i.id_crop, i.type, i.area, i.date, i.amount, i.price) for i in self.model]
        return render_template('cultivation.html', value=data)
