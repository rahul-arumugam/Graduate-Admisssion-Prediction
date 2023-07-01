import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/contact")
def contact():
    return render_template("contact.html")

@flask_app.route("/pred",methods =["GET"])
def Predict():
    return render_template("pre.html")


@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    prediction2= prediction * 100.0
    # return jsonify({'predictions':  prediction2.tolist()})
    # return render_template("pre.html", prediction_text = "The chance to get admission for Higher Studies {} %".format(prediction))
    return render_template("pre.html", prediction_text = format(prediction2))

if __name__ == "__main__":
    flask_app.run(debug=True)