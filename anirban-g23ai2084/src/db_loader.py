import pandas as pd
from sqlalchemy import create_engine

def load_to_sql(df, table_name, db_connection_string):

    try:
        engine = create_engine(db_connection_string)

        df.to_sql(table_name, engine, if_exists='replace', index=False)

        print(f"Data successfully loaded into table '{table_name}'.")

    except Exception as e:
        raise ValueError(f"Error loading data to SQL: {str(e)}")
