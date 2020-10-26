from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

mul_reg = open("credit.pkl", "rb")
ml_model = joblib.load(mul_reg)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        LIMIT_BAL = float(request.form['LIMIT_BAL'])
        EDUCATION = float(request.form['EDUCATION'])
        MARRIAGE = float(request.form['MARRIAGE'])
        AGE = float(request.form['AGE'])
        PAY_1 =float(request.form['PAY_1'])
        PAY_AMT1 = float(request.form['PAY_AMT1'])
        BILL_AMT1 = float(request.form['BILL_AMT1'])
        BILL_AMT2 = float(request.form['BILL_AMT2'])
        BILL_AMT3 = float(request.form['BILL_AMT3'])
        BILL_AMT4 = float(request.form['BILL_AMT4'])
        BILL_AMT5 = float(request.form['BILL_AMT5'])
        BILL_AMT6 = float(request.form['BILL_AMT6'])
        PAY_AMT1 = float(request.form['PAY_AMT1'])
        PAY_AMT2 = float(request.form['PAY_AMT2'])
        PAY_AMT3 = float(request.form['PAY_AMT3'])
        PAY_AMT4 = float(request.form['PAY_AMT4'])
        PAY_AMT5 = float(request.form['PAY_AMT5'])
        PAY_AMT6 = float(request.form['PAY_AMT6'])
        pred_args = [LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]
        pred_args_arr = np.array(pred_args)
        pred_args_arr = pred_args_arr.reshape(1, -1)
        mul_reg = open("credit.pkl","rb")
        ml_model = joblib.load(mul_reg)
        model_prediction = ml_model.predict(pred_args_arr)
        model_prediction = round(float(model_prediction), 2)
        if model_prediction == 0.0:
            return render_template('predict.html', prediction = " Credit card holder is Not Defaulted")
        else:
            return render_template('predict.html', prediction = " Credit card holder is Defaulted")
            

    return render_template('predict.html', prediction = model_prediction)

if __name__ == "__main__":
    app.run(debug=True)
