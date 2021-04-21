import pickle
from flask import Flask, redirect, url_for, request, jsonify
import json
import pandas as pd

app = Flask(__name__)

def load_picke_files(filename):
    obj = pickle.load(open(filename, "rb"))
    return obj

def get_prediction(input_data):
    model = load_picke_files("model.dat")
    lbl = load_picke_files("label_encoder.dat")
    te = load_picke_files("target_encoder.dat")
    input_data = pd.DataFrame(input_data)
    result = list(lbl.inverse_transform(model.predict(te.transform(input_data))))
    return result

@app.route("/predict", methods = ['POST'])
def get_pred():
    try:
        request_data = json.loads(request.data)
        result = get_prediction(request_data['data'])
        result = [{"Location":x['Location'] ,"RainFall Tommarow": y} for x, y in zip(request_data['data'], result)]
        return json.dumps(result)
    except Exception as e:
        return "something went wrong! "+str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 5000)
