# Insurance Premium Prediction
The goal of this project is to give people an estimate of premium amount based on their individual health situation. Several models were test and finally RandomForestRegressor was selected with a r2_score of 0.85. Also hyper-parameter tuning waas performed to optimize the model.

## Webpage link: [link](https://insurance111.herokuapp.com/)

## Screenshot
<img src='image/img.png' width=700 height=525>

## Tech Stack
* Front-End: HTML, Bootstrap
* Back-End: Flask
* IDE: VScode, Jupyter Notebook

## How to run the app
1. First create a virtual environment by using this command: 
   - conda create -n myenv python=3.7
2. Activate the environment using the command: 
   - conda activate myenv
3. Install the necessary packages: 
   - pip install -r requirements.txt
4. Run the app: 
   - python app.py

### Data From: [kaggle](https://www.kaggle.com/noordeen/insurance-premium-prediction)

### Data-Preprocessing:
* Check for missing values
* Categorical values handled using one-hot encoder.

### Model Selection:
* Different regressor models were tried and out of these randomforestregressor was chosen.
* Performed hyperparameter tuning using GridSearchCV to improve performance.

### Deployment:
The model is deployed using flask on heroku.


