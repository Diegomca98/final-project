from flask import Flask, render_template
import pandas as pd
import numpy as np

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
        'mean': 34,
        'std': 35,
        'min': 76,
        'max': 13,
        'quant_25': 20,
        'quant_50': 15,
        'quant_75': 100
    }

    return render_template(
        'index.html', 
        stats=stats
    )