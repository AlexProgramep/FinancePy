from flask import Blueprint, render_template, request, redirect, url_for
import yfinance as yf
from datetime import date

stocks = Blueprint('stocks', __name__, template_folder='templates')


@stocks.route("/")
def index():
    return render_template("stocks_start.html")


@stocks.route("/check", methods=['POST'])
def check():
    if request.method == 'POST':
        ticker = request.form['ticker']
        return redirect(url_for('.stocks_result', ticker=ticker))


@stocks.route("/stocks/<string:ticker>")
def stocks_result(ticker):
    today = date.today()
    ticker_name = yf.Ticker(ticker)
    ticker_csv = yf.download(ticker, start=f"{today.year - 1}-{today.month}-{today.day}")
    ticker_csv.to_csv('static\\table.csv')
    return render_template("stocks.html", ticker_name=ticker_name)
