from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import csv
import numpy as np
import pandas as pd


#model = pickle.load(open('iri.pkl', 'rb'..p))

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    dat = request.form['TransID']
    df = pd.read_csv('/content/drive/MyDrive/graphfrauddetectionworking/deployMLModel_v3/deployMLModel_v3/prediction.csv')
    res = df.loc[df['TransactionID'] == int(dat)]
    if len(res)==0:
        data = 3
    else:
        val = res['isFraud'].values[0]
        if int(val) == 0:
          data = 'Non Fraudulent Transaction'
        else:
          data = 'Fraudulent Transaction'
    return render_template('after.html', data=data)
      
@app.route('/data', methods=['POST'])
def verify():
    dat = request.form['TransID']
    df = pd.read_csv('/content/drive/MyDrive/graphfrauddetectionworking/deployMLModel_v3/deployMLModel_v3/prediction.csv')
    res = df.loc[df['TransactionID'] == int(dat)]
    if len(res)==0:
        data = 3
    else:
        data = [res['TransactionID'].values[0], res['TransactionAmt'].values[0], res['card4'].values[0], res['card6'].values[0]]
    return render_template('data.html', data=data)
      
     



if __name__ == "__main__":
  app.run()