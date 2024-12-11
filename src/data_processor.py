import numpy as np
import pandas as pd
from enums import TrainingModels
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib

scaler = StandardScaler()
 
def convert_to_dataframe(file_path):
    df = pd.DataFrame()
    # Read the Excel file
    try:
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {str(e)}")
    # We can perform other cleaning tasks here
    # We shall analyse what logic others have used for data cleaning and choose the best one here.

    return df

def prepareData(data) : 
    X = data.iloc[:, :-1]  # Features
    y = data.iloc[:, -1] # Target variable
    
    print(X,y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Fit and transform the training data
    X_train = scaler.fit_transform(X_train)

    # Transform the test data using the same scaler
    X_test = scaler.transform(X_test)

    
    
    return X_train, X_test, y_train, y_test

def train_model(data, modelType):

    match modelType:
        case TrainingModels.RandomForestRegressor:
            # Separate features and target
            X_train, X_test, y_train, y_test = prepareData(data)

            # Initialize the model
            model = RandomForestRegressor(n_estimators=100, random_state=42)

            # Train the model
            model.fit(X_train, y_train)

            # Evaluate the model
            score = model.score(X_test, y_test)
            print(f"Model R^2 Score: {score}")
            

            # Save the model
            joblib.dump(model, 'model/trained_model.pkl')


    return X_train.shape[1]

def predictMV(data) :
    # Load the model
    loaded_model = joblib.load('model/trained_model.pkl')
    sample_data = [list(data)]
    # Test prediction
    # sample_data = X_test.reshape(1, -1)  # Use a test sample
    predicted_mv = loaded_model.predict(sample_data)
    print(f"Predicted MV: {predicted_mv[0]}")
    return predicted_mv[0]

