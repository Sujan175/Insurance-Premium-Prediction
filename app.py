from flask import Flask, render_template, request
from flask import jsonify 
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('GradientBoostingRegressor.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        sex_male = request.form['sex_male']
        if(sex_male=='male'):
            sex_male=1
        else:
            sex_male=0
        smoker_yes = request.form['smoker_yes']
        if(smoker_yes=='yes'):
            smoker_yes=1
        else:
            smoker_yes=0
        region = request.form['region']
        if(region=='northwest'):
            region_northwest=1
            region_southwest=0
            region_southeast=0
        elif(region=='southeast'):
            region_northwest=0
            region_southwest=0
            region_southeast=1
        elif(region=='southwest'):
            region_northwest=0
            region_southwest=1
            region_southeast=0
        else:
            region_northwest=0
            region_southwest=0
            region_southeast=0
        
        
        prediction=model.predict([[age, bmi, children, sex_male, smoker_yes, region_northwest, region_southeast, region_southwest]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Invalid Inputs")
        else:
            return render_template('index.html',prediction_text="Insurance Premium {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
