from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd
import json


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()

    ####
    values =([['Female', 'Male'],['yes', 'no'],['no', 'yes'],['Sometimes', 'Frequently', 'Always', 'no'],['no', 'yes'],['no', 'yes'],['no', 'Sometimes', 'Frequently', 'Always'],['Public_Transportation', 'Walking', 'Automobile', 'Motorbike','Bike'],])
    index =0
    final = []
    for _ in data:
        if isinstance(_,str):
            final.append(values[index].index(_))
            index+=1
        else:
            final.append(_)
    ####
    df = pd.DataFrame(np.array(final).reshape(1,-1))
    prediction = np.array2string(model.predict(df))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = './models/final_modele.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='127.0.0.1')