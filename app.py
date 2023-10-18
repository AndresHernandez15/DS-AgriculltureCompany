from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from logic.cropController import CropController
from logic.SiloController import SiloController

app = Flask(__name__)
bootstrap = Bootstrap(app)

crop_controller = CropController()
silo_controller = SiloController()

@app.route("/")
def home():
    return render_template('index.html')


""" Crop Endpoints """


@app.route("/crop", methods=["GET"])
def crop():
    return crop_controller.crop()


@app.route('/crop_update/<id_crop>', methods=['GET'])
def crop_update(id_crop):
    return crop_controller.crop_update(id_crop)


@app.route('/crop_detail', methods=['POST'])
def crop_detail():
    return crop_controller.crop_detail()


@app.route('/cultivation')
def cultivation():
    return crop_controller.cultivation()


@app.route('/crop_delete/<id_crop>', methods=['GET'])
def crop_delete(id_crop):
    return crop_controller.crop_delete(id_crop)


""" Harvest Endpoints """


@app.route('/harvest/<id_harvest>', methods=['GET'])
def harvest(id_harvest):
    return crop_controller.harvest(id_harvest)


@app.route('/harvest_update/<id_harvest>', methods=['GET'])
def harvest_update(id_harvest):
    return crop_controller.harvest_update(id_harvest)


@app.route('/harvest_detail', methods=['POST'])
def harvest_detail():
    return crop_controller.harvest_detail()


@app.route('/harvested')
def harvested():
    return crop_controller.harvested()


@app.route('/harvest_delete/<id_harvest>', methods=['GET'])
def harvest_delete(id_harvest):
    return crop_controller.harvest_delete(id_harvest)


""" Silo Endpoints """

@app.route("/silo", methods=["GET"])
def silo():
    return silo_controller.silo()


@app.route('/silo_update/<id_silo>', methods=['GET'])
def silo_update(id_silo):
    return silo_controller.silo_update(id_silo)


@app.route('/silo_detail', methods=['POST'])
def silo_detail():
    return silo_controller.silo_detail()


@app.route('/silocreation')
def silocreation():
    return silo_controller.silocreation()


@app.route('/silo_delete/<id_silo>', methods=['GET'])
def silo_delete(id_silo):
    return silo_controller.silo_delete(id_silo)


""" Product Endpoints """


@app.route('/product/<id_product>', methods=['GET'])
def product(id_product):
    return silo_controller.product(id_product)


@app.route('/product_update/<id_product>', methods=['GET'])
def product_update(id_product):
    return silo_controller.product_update(id_product)


@app.route('/product_detail', methods=['POST'])
def product_detail():
    return silo_controller.product_detail()


@app.route('/productcreation')
def products():
    return silo_controller.products()


@app.route('/product_delete/<id_product>', methods=['GET'])
def product_delete(id_product):
    return silo_controller.product_delete(id_product)


if __name__ == '__main__':
    app.run()
