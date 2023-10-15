from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return "Hola mundo!"


if __name__ == '__main__':
    app.run()
