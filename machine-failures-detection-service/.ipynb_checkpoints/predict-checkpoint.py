import pickle
import xgboost
from flask import Flask, request, jsonify

input = 'xgb_clf.bin'

with open(input, 'rb') as f:
    model, dv = pickle.load(f)

app = Flask('machine-failure-detection-service')

@app.route('/predict', methods=['POST'])
def predict():
    machine_condition = request.get_json()
    X = dv.transform([machine_condition])
    dX = xgboost.DMatrix(X, feature_names=dv.feature_names_)

    y_pred = model.predict(dX)
    failure = y_pred >= 0.5

    result = {
        'failure': bool(failure),
        'failure_probability': float(y_pred)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)