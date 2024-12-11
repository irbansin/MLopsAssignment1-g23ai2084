
import pandas as pd
from flask import Flask, render_template, request, jsonify 
import os
from data_processor import convert_to_dataframe, predictMV, train_model  # Import the data processing function
from enums import TrainingModels


app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Google Cloud SQL Connection String
DB_CONNECTION_STRING = 'postgresql://postgres:dadu.007@34.93.188.48:5432/airbnb-master'

etlRunning = False

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/upload')
def upload_page():
    return render_template('pages/upload.html')

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'message': 'No file part in the request'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

    
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        try:
            df = convert_to_dataframe(file_path) # takes in file and trains a model
            numberOfInputs = train_model(df, TrainingModels.RandomForestRegressor)

            return jsonify({'message': {'x_columns': numberOfInputs}}), 200
        except Exception as e:
            return jsonify({'message': f'Error processing file: {str(e)}'}), 500
    except:
        return jsonify({'message': 'Invalid file format. Please upload an Excel file.'}), 400

@app.route('/getPrediction', methods=['POST'])
def getPrediction():
    try:
        form_data = request.form.to_dict()
        featuresTuple = list(form_data.values())
        featuresTupleRectified = [float(item if item != '' else '0') for item in featuresTuple]
        mvValue = predictMV(featuresTupleRectified)
        return  jsonify({'message': {'mvValue': mvValue}}), 200
    except Exception as e:
        return jsonify({'message': f'Error Predicting MV value: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
