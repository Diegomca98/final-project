from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import RobustScaler, MinMaxScaler
from pickle import load

app = Flask(__name__)

# For model_deploy view

model = load(
    open(
        '../models/svc_model-C-1_gamma-001_kernel-rbf_max-iter-500_rand-state-42.sav', 
        'rb'
    )
)

airports = pd.read_csv('../data/webapp/airports.csv')
airlines = pd.read_csv('../data/webapp/airlines_prediction.csv')
scale_for_model = pd.read_csv('../data/webapp/scale_for_model.csv')

# For model_deploy view

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
    g = [
        'arr_delay_by_airline.png',
        'arr_dep_delay-less-30.png',
        'eda-cat_values.png', #
        'eda-cat_values0.png', #
        'eda-correlation.png', #
        'eda-numerical.png'
    ]

    return render_template(
        'single.html',
        title = 'Fly Me! - Exploratory Data Analysis',
        visuals = g,
        banner_title = 'Exploratory Data Analysis',
        breadcrumb = 'EDA',
        view_name = 'eda_data'
    )

@app.route('/model', methods=['GET', 'POST'])
def model_deploy():
    selected_columns = [
        'OriginAirportID',
        'DestAirportID',
        'Airline',
        'OriginCityName',
        'Distance',
        'AirTime',
        'Month'
    ]

    months_of_year = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }

    return render_template(
        'model.html',
        title = 'Fly Me! - Model',
        visuals = os.listdir('./static/graphs'),
        banner_title = 'Try Out Our Model',
        breadcrumb = 'MODEL',
        view_name = 'model_deploy',
        columns = selected_columns,
        months = months_of_year,
        airports_cities = airports,
        airlines = airlines,
    )

@app.route('/predict', methods=['POST'])
def predict():
    class_dict = {
        '0': 'Early',
        '1': 'On-Time',
        '2': 'Late',
    }
    mins_dict = {
        'OriginAirportID': 0,
        'DestAirportID': 0,
        'Airline': 0,
        'OriginCityName': 0,
        'Distance': 31.0,
        'AirTime': 8.0,
        'Month': 1,
    }

    max_dict = {
        'OriginAirportID': 373,
        'DestAirportID': 373,
        'Airline': 20,
        'OriginCityName': 367,
        'Distance': 5095.0,
        'AirTime': 673.0,
        'Month': 7
    }
    
    median_dict = {
        'OriginAirportID': 32,
        'DestAirportID': 40,
        'Airline': 3,
        'OriginCityName': 27,
        'Distance': 646.0,
        'AirTime': 94.0,
        'Month': 4,
    }
    iqr_dict = {
        'OriginAirportID': 62,
        'DestAirportID': 59,
        'Airline': 7,
        'OriginCityName': 59,
        'Distance': 667.0,
        'AirTime': 81.0,
        'Month': 4,
    }



    max_series = pd.Series(max_dict)
    min_series = pd.Series(mins_dict)
    median_series = pd.Series(median_dict)
    iqr_series = pd.Series(iqr_dict)

    origin_airport_ID = int(request.form['origin_airport_ID'])
    dest_airport_ID = int(request.form['dest_airport_ID'])

    airline = int(request.form['airline'])
    origin_city_name = int(request.form['city'])
    distance = float(request.form['distance'])
    air_time = float(request.form['f_duration'])
    month = int(request.form['month'])

    pred_dict = {
        'OriginAirportID': origin_airport_ID,
        'DestAirportID': dest_airport_ID,
        'Airline': airline,
        'OriginCityName': origin_city_name,
        'Distance': distance,
        'AirTime': air_time,
        'Month': month
    }

    # Apply scaling
    df = pd.DataFrame([pred_dict])
    scaled_data = (df - median_series) / iqr_series
    

    dict_for_pred = {
        'OriginAirportID': int(scaled_data.iloc[0]['OriginAirportID']),
        'DestAirportID': int(scaled_data.iloc[0]['DestAirportID']),
        'Airline': int(scaled_data.iloc[0]['Airline']),
        'OriginCityName': int(scaled_data.iloc[0]['OriginCityName']),
        'Distance': int(scaled_data.iloc[0]['Distance']),
        'AirTime': int(scaled_data.iloc[0]['AirTime']),
        'Month': int(scaled_data.iloc[0]['OriginAirportID'])
    }


    # Make prediction using the model
    prediction = str(int(model.predict(scaled_data)))
    
    #Perform model prediction with the selected AirportID
    return render_template(
        'prediction.html',
        pred_dict = pred_dict,
        df = df,
        scaled = type(scaled_data),
        prediction = prediction,
        banner_title = "Most likely you're going to arrive",
        text = class_dict[prediction],
        breadcrumb = 'MODEL',
        view_name = 'model_deploy',
        pred = True
    )