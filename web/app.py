from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from logic.cropController import CropController

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []

crop_controller = CropController()


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


if __name__ == '__main__':
    app.run()
