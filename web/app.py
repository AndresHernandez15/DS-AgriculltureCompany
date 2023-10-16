from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.cropController import CropController

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []

crop_controller = CropController()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/crop", methods=["GET"])
def crop():
    return crop_controller.crop()


@app.route('/crop_detail', methods=['POST'])
def crop_detail():
    return crop_controller.crop_detail()


@app.route('/cultivation')
def cultivation():
    return crop_controller.cultivation()


@app.route('/crop_update/<id_crop>', methods=['GET'])
def crop_update(id_crop):
    return crop_controller.crop_update(id_crop)


@app.route('/crop_delete/<id_crop>', methods=['GET'])
def crop_delete(id_crop):
    return crop_controller.crop_delete(id_crop)


if __name__ == '__main__':
    app.run()
