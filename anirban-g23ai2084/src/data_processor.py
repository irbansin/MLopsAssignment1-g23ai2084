import pandas as pd

def process_excel_file(file_path):


    # Read the Excel file
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {str(e)}")

    # drop rows with missing values. Write a file with a better logic here
    df_cleaned = df.dropna()


    # We can perform other cleaning tasks here

    return df_cleaned
