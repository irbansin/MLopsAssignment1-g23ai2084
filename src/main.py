from flask import Flask, render_template, request, jsonify
import os
from data_processor import process_excel_file  # Import the data processing function
from db_loader import load_to_sql  # Import the database loader function
from etl import etl


app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Google Cloud SQL Connection String
DB_CONNECTION_STRING = 'postgresql://postgres:dadu.007@34.93.188.48:5432/airbnb-master'

# finalData = etl()
# load_to_sql(finalData, 'master', DB_CONNECTION_STRING)

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
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and file.filename.endswith('.xlsx'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        try:
            cleaned_data = process_excel_file(file_path)

            # Load the cleaned data into Google Cloud file_pathSQL
            table_name = os.path.splitext(file.filename)[0]  
            load_to_sql(cleaned_data, table_name, DB_CONNECTION_STRING)

            return jsonify({'message': 'File uploaded and loaded into Google Cloud SQL successfully'}), 200
        except Exception as e:
            return jsonify({'message': f'Error processing file: {str(e)}'}), 500

    return jsonify({'message': 'Invalid file format. Please upload an Excel file.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
