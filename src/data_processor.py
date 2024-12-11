import pandas as pd
from enums import TrainingModels

def convert_to_dataframe(file_path):
    df
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


def train_model(data, modelType):
    match modelType:
        case TrainingModels.RandomForestRegressor:
            # Separate features and target
            X = data.iloc[:, :-1]  # Features
            y = data.iloc[:, -1] # Target variable
            
            print(X,y)




