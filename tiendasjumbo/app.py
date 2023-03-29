from flask import Flask, request, jsonify
from scrapy import cmdline
import json
from multiprocessing import Process
import os
import time
import datetime


app = Flask(__name__)

def scrape_data(url,jsonName):
    cmdline.execute(["scrapy", "crawl", "productos", "-a", "externalUrl="+url, "-o", jsonName])

@app.route('/', methods=['GET'])
def index():
    return '''
        <form method="POST">
            <label for="url">Ingresa una URL:</label>
            <input type="text" name="url" id="url">
            <input type="submit" value="Enviar">
        </form>
    '''

@app.route('/', methods=['POST'])
def scrape():
    url = request.form['url']

    date=datetime.datetime.now()
    dateYmd= date.date().strftime('%Y-%m-%d')
    hour= date.strftime('%H_%M_%S')
    jsonName=dateYmd+'__'+hour+'.json'

    # Ejecutar el scraping en un proceso hijo
    p = Process(target=scrape_data, args=(url,jsonName))
    p.start()
    p.join()

    # esperear a que el archivo exista
    while not os.path.exists(jsonName):
        time.sleep(5)

    # Leer el archivo generado por el scraping
    with open(jsonName) as file:
        data = json.load(file)

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)