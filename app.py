from flask import Flask, render_template
from stocks.blueprint import stocks
from crypto.blueprint import crypto
from currency.blueprint import currency

app = Flask(__name__)
app.debug = False
app.register_blueprint(stocks, url_prefix="/stocks")
app.register_blueprint(crypto, url_prefix="/crypto")
app.register_blueprint(currency, url_prefix="/currency")

host = "localhost"
port = 5000


@app.route("/")
def start_page():
    return render_template("index.html")


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=host, port=port)
