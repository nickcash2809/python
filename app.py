import request
import configparser

from flask import Flask, render_template, request

app = flask (_name_)

if _name_=="_main_":
    app.run(debug=True)

    #ruta resultados
    @app.route('/')
    def weather_dashboard():
        retur render_template ('homme.html')


    #ruta ingreso de ciudad
    @app.route ('/results')
    def render_resultados
        cityname=request.form ['cityname']

        api = get_api_key();

        #data contiente jason con la respuestas

        data = get_weather_results(Cityname, api)

        #se toma la temperatura del json

        temp = "{0:2f}"format (data['main']['temp'])


    #aqui se consume servicio web 

    def get_weather_results (Cityname, api_key)

        url = "https://api.openwathermap.org/data/2.5/weather?q={}&appid={}".format(Cityname, api_key)

        r = request.get(url)
        return r.json


    def get_api_key ():
        #consumir servicio web con api key
        config = configparser.configparser()

        config.read ('config.ini')
        return config ['openweathermap']['api']