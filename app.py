from flask import Flask, render_template, request
from datetime import datetime
from logic.controller import Controller

app = Flask(__name__)
controller = Controller()

controller.load_from_json('data.json')

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/about_us", methods=["GET"])
def about_us():
    return render_template('about_us.html')

@app.route("/contact", methods=["GET"])
def contact_us():
    return render_template('contact_us.html')


""" Crop Endpoints """

@app.route("/crop", methods=["GET"])
def get_crop():
    return controller.crop()

@app.route('/crop_update/<int:id_crop>', methods=['GET'])
def get_crop_update(id_crop):
    return controller.crop_update(id_crop)

@app.route('/crop_detail', methods=['POST'])
def post_crop_detail():
    op = request.form['op']
    id_crop = int(request.form['id_crop'])
    crop_type = request.form['crop_type']
    area = float(request.form['area'])
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    amount = int(request.form['amount'])
    price = float(request.form['price'])
    return controller.crop_detail(op, id_crop, crop_type, area, date, amount, price)

@app.route('/cultivation', methods=['GET'])
def get_cultivation():
    return controller.cultivation()

@app.route('/crop_delete/<int:id_crop>', methods=['GET'])
def get_crop_delete(id_crop):
    return controller.crop_delete(id_crop)

""" Harvest Endpoints """

@app.route('/harvest/<int:id_harvest>', methods=['GET'])
def get_harvest(id_harvest):
    return controller.harvest(id_harvest)

@app.route('/harvest_update/<int:id_harvest>', methods=['GET'])
def get_harvest_update(id_harvest):
    return controller.harvest_update(id_harvest)

@app.route('/harvest_detail', methods=['POST'])
def post_harvest_detail():
    op = request.form['op']
    id_harvest = int(request.form['id_harvest'])
    crop_type = request.form['crop_type']
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    weight = float(request.form['weight'])
    return controller.harvest_detail(op, id_harvest, crop_type, date, weight)

@app.route('/harvested', methods=['GET'])
def get_harvested():
    return controller.harvested()

@app.route('/harvest_delete/<int:id_harvest>', methods=['GET'])
def get_harvest_delete(id_harvest):
    return controller.harvest_delete(id_harvest)

""" Silo Endpoints """

@app.route("/silo", methods=["GET"])
def get_silo():
    return controller.silo()

@app.route('/silo_update/<int:id_silo>', methods=['GET'])
def get_silo_update(id_silo):
    return controller.silo_update(id_silo)

@app.route('/silo_detail', methods=['POST'])
def post_silo_detail():
    op = request.form['op']
    capacity = int(request.form['capacity'])
    return controller.silo_detail(op, capacity)

@app.route('/silocreation', methods=['GET'])
def get_silocreation():
    return controller.silocreation()

@app.route('/silo_delete/<int:id_silo>', methods=['GET'])
def get_silo_delete(id_silo):
    return controller.silo_delete(id_silo)

""" Product Endpoints """

@app.route('/product/<int:id_product>', methods=['GET'])
def get_product(id_product):
    return controller.product(id_product)

@app.route('/product_detail', methods=['POST'])
def post_product_detail():
    op = request.form['op']
    silo = int(request.form['silo'])
    id_product = int(request.form['id_product'])
    product_type = request.form['product_type']
    weight = float(request.form['weight'])
    sellprice = float(request.form['sellprice'])
    amount = int(request.form['amount'])
    return controller.product_detail(op, silo, id_product, product_type, weight, sellprice, amount)

@app.route('/productcreation', methods=['GET'])
def get_products():
    return controller.products()

@app.route('/product_delete/<int:id_product>', methods=['GET'])
def get_product_delete(id_product):
    return controller.product_delete(id_product)

@app.route('/show_products/<int:id_silo>', methods=['GET'])
def get_product_show(id_silo):
    return controller.show_products(id_silo)


@app.teardown_appcontext
def save_data_on_shutdown(error=None):
    controller.save_to_json('data.json')

if __name__ == '__main__':
    app.run(debug=True)
