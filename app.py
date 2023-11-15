from datetime import datetime

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from logic.controller import Controller

app = FastAPI()
controller = Controller()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.get("/about_us", response_class=HTMLResponse)
def about_us(request: Request):
    return templates.TemplateResponse('about_us.html', {"request": request})


@app.get("/contact", response_class=HTMLResponse)
def contact_us(request: Request):
    return templates.TemplateResponse('contact_us.html', {"request": request})


""" Crop Endpoints """


@app.get("/crop", response_class=HTMLResponse)
def get_crop(request: Request):
    return controller.crop(request)


@app.get('/crop_update/{id_crop}', response_class=HTMLResponse)
def get_crop_update(id_crop: int, request: Request):
    return controller.crop_update(id_crop, request)


@app.post('/crop_detail', response_class=HTMLResponse)
def post_crop_detail(request: Request, op: str = Form(...), id_crop: int = Form(...),
                     crop_type: str = Form(...), area: float = Form(...),
                     date: str = Form(...), amount: int = Form(...), price: float = Form(...)):
    return controller.crop_detail(request, op, id_crop, crop_type, area, datetime.strptime(date, "%Y-%m-%d"),
                                  amount, price)


@app.get('/cultivation', response_class=HTMLResponse)
def get_cultivation(request: Request):
    return controller.cultivation(request)


@app.get('/crop_delete/{id_crop}', response_class=HTMLResponse)
def get_crop_delete(id_crop: int, request: Request):
    return controller.crop_delete(id_crop, request)


""" Harvest Endpoints """


@app.get('/harvest/{id_harvest}', response_class=HTMLResponse)
def get_harvest(id_harvest: int, request: Request):
    return controller.harvest(id_harvest, request)


@app.get('/harvest_update/{id_harvest}', response_class=HTMLResponse)
def get_harvest_update(id_harvest: int, request: Request):
    return controller.harvest_update(id_harvest, request)


@app.post('/harvest_detail', response_class=HTMLResponse)
def post_harvest_detail(request: Request, op: str = Form(...), id_harvest: int = Form(...),
                        crop_type: str = Form(...), date: str = Form(...), weight: float = Form(...)):
    return controller.harvest_detail(request, op, id_harvest, crop_type, datetime.strptime(date, "%Y-%m-%d"),
                                     weight)


@app.get('/harvested', response_class=HTMLResponse)
def get_harvested(request: Request):
    return controller.harvested(request)


@app.get('/harvest_delete/{id_harvest}', response_class=HTMLResponse)
def get_harvest_delete(id_harvest: int, request: Request):
    return controller.harvest_delete(id_harvest, request)


""" Silo Endpoints """


@app.get('/silo', response_class=HTMLResponse)
def get_silo(request: Request):
    return controller.silo(request)


@app.get('/silo_update/{id_silo}', response_class=HTMLResponse)
def get_silo_update(id_silo: int, request: Request):
    return controller.silo_update(id_silo, request)


@app.post('/silo_detail', response_class=HTMLResponse)
def post_silo_detail(request: Request, op: str = Form(...), capacity: int = Form(...)):
    return controller.silo_detail(request, op, capacity)


@app.get('/silocreation', response_class=HTMLResponse)
def get_silocreation(request: Request):
    return controller.silocreation(request)


@app.get('/silo_delete/{id_silo}', response_class=HTMLResponse)
def get_silo_delete(id_silo: int, request: Request):
    return controller.silo_delete(id_silo, request)


""" Product Endpoints """


@app.get('/product/{id_product}', response_class=HTMLResponse)
def get_product(id_product: int, request: Request):
    return controller.product(id_product, request)


@app.post('/product_detail', response_class=HTMLResponse)
def post_product_detail(request: Request, op: str = Form(...), silo: int = Form(...), id_product: int = Form(...),
                        product_type: str = Form(...), weight: float = Form(...), sellprice: float = Form(...),
                        amount: int = Form(...)):
    return controller.product_detail(request, op, silo, id_product, product_type, weight, sellprice, amount)


@app.get('/productcreation', response_class=HTMLResponse)
def get_products(request: Request):
    return controller.products(request)


@app.get('/product_delete/{id_product}', response_class=HTMLResponse)
def get_product_delete(id_product: int, request: Request):
    return controller.product_delete(id_product, request)


@app.get('/show_products/{id_silo}', response_class=HTMLResponse)
def get_product_show(id_silo: int, request: Request):
    return controller.show_products(id_silo, request)


if __name__ == "__main__":
    uvicorn.run('app:app')
