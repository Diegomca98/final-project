from flask import Flask, render_template
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

#df = pd.read_csv('../data/raw/test-webapp.csv')
# stats = {
#     'mean': df.ArrTime.mean(),
#     'std': df.ArrTime.std(),
#     'min': df.ArrTime.min(),
#     'max': df.ArrTime.max(),
#     '25': df.ArrTime.quantile(0.25),
#     '50': df.ArrTime.quantile(0.50),
#     '75': df.ArrTime.quantile(0.75),
# }

@app.route('/')
def index():
    stats = {
        'mean': 7.609537,
        'std': 55.430586,
        'min': -91.000000,
        'max': 2678.000000,
        'quant_25': -14.000000,
        'quant_50': -5.000000,
        'quant_75': 10.000000
    }
    inferences = {
        'months_less_flights': 'The month with less flights is February, which is directly related to the amount of days in the month.',
        'cancels_divertions': 'Most flights are not cancelled nor diverted, but cancellations have the most occurences between those 2 categories.',
        'dup_values': 'Some columns are pretty much duplicates which had to be dropped, for example columns like IATA_Code_Operating_Airline and IATA_Code_Operating_Airline',
        'Categorial': 'Airline, DepTime, ArrTime, Marketing_Airline_Network, Operated_or_Branded_Code_Share_Partners, Operating_Airline, Cancelled',
        'Numerical': 'DepDelay, AirTime, Distance, Month, DOT_ID_Marketing_Airline, Flight_Number_Marketing_Airline, DOT_ID_Operating_Airline, Flight_Number_Operating_Airline, OriginAirportID, DestAirportID, ArrDelay, DivAirportLandings',
    }

    counters = {
        'columns': 38,
        'hours_spent': 8*25,
        'records': 500000,
        'coffee_cups': 5*25,
    }

    return render_template(
        'index.html', 
        title = 'Fly Me! - Flight Prediction Model',
        stats = stats,
        desc_analysis = inferences,
        counters = counters,
    )

@app.route('/eda')
def eda_data():
    graphs = os.listdir('./static/graphs')

    return render_template(
        'single.html',
        title = 'Fly Me! - Exploratory Data Analysis',
        visuals = graphs
    )