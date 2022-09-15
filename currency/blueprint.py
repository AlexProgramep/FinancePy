from flask import Blueprint, render_template, request, redirect, url_for
from py_currency_converter import convert

currency = Blueprint('currency', __name__, template_folder='templates')


@currency.route("/")
def index():
    return render_template("currency_start.html")


@currency.route("/check", methods=['POST'])
def check_currency():
    if request.method == 'POST':
        curr = request.form['currency']
        return redirect(url_for('.cur', curr=curr))


@currency.route("/currency/<string:curr>")
def cur(curr):
    curr_value = convert(amount=1, to=[str(curr)])[str(curr)]
    return render_template("currency.html", curr_name=curr, curr_value=curr_value)
