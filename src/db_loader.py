import pandas as pd
from sqlalchemy import create_engine, text

def load_to_sql(df, table_name, db_connection_string):

    try:
        engine = create_engine(db_connection_string, echo=True)
        with engine.begin() as connection:
            df.to_sql(table_name,con=connection,  if_exists='replace', index=True)

        print(f"Data successfully loaded into table '{table_name}'.")

    except Exception as e:
        raise ValueError(f"Error loading data to SQL: {str(e)}")
