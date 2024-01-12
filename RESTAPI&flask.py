from flask import Flask,jsonify
from bs4 import BeautifulSoup as bs
import requests
def get_rate(in_curr,out_curr):
    url=f"https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1"
    response = requests.get(url).text
    content=bs(response,'html.parser')
    value=content.find('span',"ccOutputRslt").text
    return value[:-4]

app = Flask(__name__)
@app.route('/')
def currency_converter():
    return "<h1>CURRENCY CONVERTOR</h1>"
@app.route('/api/<in_cur>-<out_cur>')
def rate_converter(in_cur, out_cur):
    rate=get_rate(in_cur,out_cur)
    dicty={"In_curr": in_cur, "Out_cur": out_cur, "rate": rate}
    return jsonify(dicty)
app.run()