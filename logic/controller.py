from datetime import datetime

from fastapi import Request, Form
from fastapi.templating import Jinja2Templates

from logic.crop import Crop
from logic.harvest import Harvest
from logic.silo import Silo
from logic.product import Product

templates = Jinja2Templates(directory="templates")


class Controller:
    def __init__(self):
        self.crops = []
        self.harvests = []
        self.silos = []

    """ Crop Methods """

    def crop(self, request: Request):
        return templates.TemplateResponse('crop.html', {"request": request})

    def crop_update(self, id_crop: int, request: Request):
        return templates.TemplateResponse('crop_update.html', {"request": request, "id_crop": id_crop})

    def crop_detail(self, request: Request, op: str = Form(...), id_crop: int = Form(...),
                    crop_type: str = Form(...), area: float = Form(...),
                    date: datetime = Form(...), amount: int = Form(...), price: float = Form(...)):
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

        return templates.TemplateResponse('crop_detail.html', {"request": request, "value": c})

    def cultivation(self, request: Request):
        data = [(i.id_crop, i.type, i.area, i.date, i.amount, i.price) for i in self.crops]
        return templates.TemplateResponse('cultivation.html', {"request": request, "value": data})

    def crop_delete(self, id_crop: int, request: Request):
        self.crops = [i for i in self.crops if i.id_crop != id_crop]
        data = [(i.id_crop, i.type, i.area, i.date, i.amount, i.price) for i in self.crops]
        return templates.TemplateResponse('cultivation.html', {"request": request, "value": data})

    """ Harvest Methods """

    def harvest(self, id_harvest: int, request: Request):
        return templates.TemplateResponse('harvest.html', {"request": request, "id_harvest": id_harvest})

    def harvest_update(self, id_harvest: int, request: Request):
        return templates.TemplateResponse('harvest_update.html', {"request": request, "id_harvest": id_harvest})

    def harvest_detail(self, request: Request, op: str = Form(...), id_harvest: int = Form(...),
                       crop_type: str = Form(...), date: datetime = Form(...), weight: float = Form(...)):
        h = Harvest(id_harvest=id_harvest, type=crop_type, date=date, weight=weight)
        print(h)
        if op == 'I':
            self.harvests.append(h)
            self.crops = [crop for crop in self.crops if crop.id_crop != id_harvest]
        elif op == 'U':
            for row in self.harvests:
                if row.id_harvest == id_harvest:
                    row.type = crop_type
                    row.date = date
                    row.weight = weight
                    break

        return templates.TemplateResponse('harvest_detail.html', {"request": request, "value": h})

    def harvested(self, request: Request):
        data = [(i.id_harvest, i.type, i.date, i.weight) for i in self.harvests]
        return templates.TemplateResponse('harvested.html', {"request": request, "value": data})

    def harvest_delete(self, id_harvest: int, request: Request):
        self.harvests = [i for i in self.harvests if i.id_harvest != id_harvest]
        data = [(i.id_harvest, i.type, i.date, i.weight) for i in self.harvests]
        return templates.TemplateResponse('harvested.html', {"request": request, "value": data})

    """ Silo Methods """

    def silo(self, request: Request):
        return templates.TemplateResponse('silo.html', {"request": request})

    def silo_update(self, id_silo: int, request: Request):
        return templates.TemplateResponse('silo_update.html', {"request": request, "id_silo": id_silo})

    def silocreation(self, request: Request):
        data = [(s.id_silo, s.capacity) for s in self.silos]
        return templates.TemplateResponse('silocreation.html', {"request": request, "value": data})

    def silo_detail(self, request: Request, op: str = Form(...), capacity: int = Form(...)):
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

        return templates.TemplateResponse('silo_detail.html', {"request": request, "value": s})

    def silo_delete(self, id_silo: int, request: Request):
        self.silos = [s for s in self.silos if s.id_silo != id_silo]
        data = [(s.id_silo, s.capacity) for s in self.silos]
        return templates.TemplateResponse('silocreation.html', {"request": request, "value": data})

    """ Product Methods """

    def product(self, id_product: int, request: Request):
        return templates.TemplateResponse('product.html', {"request": request, "id_product": id_product})

    def product_detail(self, request: Request, op: str = Form(...), silo: int = Form(...), id_product: int = Form(...),
                       product_type: str = Form(...), weight: float = Form(...), sellprice: float = Form(...),
                       amount: int = Form(...)):
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
                return templates.TemplateResponse('silofull.html', {"request": request})

        return templates.TemplateResponse('product_detail.html', {"request": request, "value": p, "value2": silo})


    def products(self, request: Request):
        data = []
        for row in self.silos:
            for col in row.products:
                data.append(col)
        return templates.TemplateResponse('productcreation.html', {"request": request, "value": data})

    def product_delete(self, id_product: int, request: Request):
        data = []
        for row in self.silos:
            for col in row.products:
                if col.id_product == id_product:
                    row.products.remove(col)
                data.append(col)

        return templates.TemplateResponse('productcreation.html', {"request": request, "value": data})

    def show_products(self, id_silo: int, request: Request):
        target_silo = None
        for silo in self.silos:
            if silo.id_silo == id_silo:
                target_silo = silo
                break

        if target_silo is not None:
            products = target_silo.products
            return templates.TemplateResponse('show_product.html', {"request": request, "value": products})
        else:
            return templates.TemplateResponse('silo_not_found.html', {"request": request})
