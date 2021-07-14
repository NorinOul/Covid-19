from flask import Flask,jsonify
import requests

app = Flask(__name__)

@app.route('/totalCovidThailand')
def totalCovidThailand():
    Data = {
        "totalCases":[],
        "totalRecovered": [],
        "totalDeaths": [],
        "activeCases": []
    }
    country = 'Thailand'
    url = 'https://disease.sh/v3/covid-19/countries/' + country
    data = requests.get(url).json()
    Data["totalCases"] = data["cases"]
    Data["totalRecovered"] = data["recovered"]
    Data["totalDeaths"] = data["deaths"]
    Data["activeCases"] = data["active"]
    return Data

@app.route('/dailyCovidThailand')
def dailyCovidThailand():
    Data = {
        "todayCases":[],
        "todayRecovered": [],
        "todayDeaths": []
    }
    country = 'Thailand'
    url = 'https://disease.sh/v3/covid-19/countries/' + country
    data = requests.get(url).json()
    Data["todayCases"] = data["todayCases"]
    Data["todayRecovered"] = data["todayRecovered"]
    Data["todayDeaths"] = data["todayDeaths"]
    return Data

@app.route('/totalCovidWorld')
def totalCovidWorld ():
    Data = {
        "totalCases":[],
        "totalRecovered": [],
        "totalDeaths": [],
        "activeCases": []
    }
    url = 'https://disease.sh/v3/covid-19/all'
    data = requests.get(url).json()
    Data["totalCases"] = data["cases"]
    Data["totalRecovered"] = data["recovered"]
    Data["totalDeaths"] = data["deaths"]
    Data["activeCases"] = data["active"]
    return Data

@app.route('/dailyCovidWorld')
def dailyCovidWorld():
    Data = {
        "todayCases":[],
        "todayRecovered": [],
        "todayDeaths": []
    }
    url = 'https://disease.sh/v3/covid-19/all'
    data = requests.get(url).json()
    Data["todayCases"] = data["todayCases"]
    Data["todayRecovered"] = data["todayRecovered"]
    Data["todayDeaths"] = data["todayDeaths"]
    return Data