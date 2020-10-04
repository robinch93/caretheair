from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

# read the model generated file and store in model variable
model1 = pickle.load(open('model1.pkl','rb'))
model2 = pickle.load(open('model2.pkl','rb'))

@app.route('/pollution')
def pollution():
    return render_template("pollution.html")

@app.route('/predictPollution',methods=['POST','GET'])
def predictPollution():

    int_features=[int(x) for x in request.form.values()]



    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model1.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('pollution.html',predDisease='Pollutant gases level in air are high. \n Probability of affecting people (with Lung Cancer, Heart Disease, Pulmonary Disease and Respiratory Infection) is {}. \n Click on "Notify Patients" button to send notification to concerned people. '.format(output))
    else:
        return render_template('pollution.html',predDisease='Pollution levels are low.\n Probability of affecting people (with Lung Cancer, Heart Disease, Pulmonary Disease and Respiratory Infection) is {}'.format(output))

@app.route('/vegetation')
def vegetation():
    return render_template("vegetation.html")

@app.route('/predictVegetation',methods=['POST','GET'])
def predictVegetation():
    int_features=[int(x) for x in request.form.values()]  # run for loop for all values in the form and converting theminto integer list.

    final=[np.array(int_features)]  # convert those integer values into numpy array.
    print(int_features)
    print(final)
    prediction=model2.predict_proba(final)   # we give that numpy array to the model.
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('vegetation.html',predVegetation='Environment is suitable for planting pollution absorbent plants. \nProbability of absorption of pollutants is  {}. \n Click on "Notify Farmers" button to send notification to concerned people. '.format(output))
    else:
        return render_template('vegetation.html',predVegetation='Environment is not suitable for planting pollution absorbent plants. \n Probability of absorption of pollutants is {}'.format(output))

@app.route('/notifyPatients')
def notifyPatients():
    return render_template("notifyPatients.html")

@app.route('/notifyFarmers')
def notifyFarmers():
    return render_template("notifyFarmers.html")

if __name__ == '__main__':
    app.run(debug=True)
