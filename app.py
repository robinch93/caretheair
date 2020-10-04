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
    int_features=[int(x) for x in request.form.values()]  # run for loop for all values in the form and converting theminto integer list.

    final=[np.array(int_features)]  # convert those integer values into numpy array.
    print(int_features)
    print(final)
    prediction=model1.predict_proba(final)   # we give that numpy array to the model.
    output='{0:.{1}f}'.format(prediction[0][1], 2)   #formats a decimal value and puts that till two decimal place.

    if output>str(0.5):    # if output is less than 0.5 it means forest is in danger.
        return render_template('pollution.html',predDisease='Your Health is in Danger.\nProbability of disease is {}'.format(output),bhai="need to do something now?")
    else:
        return render_template('pollution.html',predDisease='Your Health is safe.\n Probability of disease is {}'.format(output),bhai="Your Health is Safe for now")

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
    output='{0:.{1}f}'.format(prediction[0][1], 2)   #formats a decimal value and puts that till two decimal place.

    if output>str(0.5):    # if output is less than 0.5 it means forest is in danger.
        return render_template('vegetation.html',predVegetation='Environment is suitable for planting. \nProbability of absorption of pollutants is  {}'.format(output),bhai="kuch karna hain iska ab?")
    else:
        return render_template('vegetation.html',predVegetation='Environment not suitable for plantation. \n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")

@app.route('/notifyPatients')
def notifyPatients():
    return render_template("notifyPatients.html")

@app.route('/notifyFarmers')
def notifyFarmers():
    return render_template("notifyFarmers.html")

if __name__ == '__main__':
    app.run(debug=True)
