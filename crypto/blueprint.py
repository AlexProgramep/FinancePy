from flask import Blueprint, render_template, request, redirect, url_for
from pycoingecko import CoinGeckoAPI

crypto = Blueprint('crypto', __name__, template_folder='templates')

cg = CoinGeckoAPI()
crypto_currency = 'USD'
crypto_currency = crypto_currency.lower()


@crypto.route("/")
def index():
    return render_template("crypto_start.html")


@crypto.route("/check", methods=['POST'])
def check_crypto():
    if request.method == 'POST':
        crypto = request.form['crypto'].lower()
        return redirect(url_for('.crypto_value', crypto=crypto))


@crypto.route("/crypto/<string:crypto>")
def crypto_value(crypto):
    get_price = cg.get_price(ids=[str(crypto)], vs_currencies=[crypto_currency])[str(crypto)][str(crypto_currency)]
    return render_template("crypto.html", get_price=get_price, crypto_name=crypto)
