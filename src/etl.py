import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.impute import KNNImputer
import kagglehub
path = kagglehub.dataset_download("alexanderfreberg/airbnb-listings-2016-dataset")

print("Path to dataset files:", path)

def etl():
    print("Path to dataset files:", path)

    #------------------------Listings----------------------
    listings = pd.read_excel(path + "/Tableau Full Project.xlsx", sheet_name="Listings")
    listings = listings.dropna(subset=['weekly_price', 'monthly_price'])
    listings['host_acceptance_rate'] = listings['host_acceptance_rate'].fillna(0)
    listings['host_response_rate'] = listings['host_response_rate'].fillna(0)
    listings['review_scores_checkin'] = listings['review_scores_checkin'].fillna(7)
    listings['review_scores_communication'] = listings['review_scores_communication'].fillna(7)
    listings['bathrooms'] = listings['bathrooms'].fillna(1)
    listings['bathrooms'] = listings['bathrooms'].apply(lambda x: int(x))
    
    #------------------------Calendar----------------------
    calendar = pd.read_excel(path + "/Tableau Full Project.xlsx", sheet_name="Calendar")
    imputer = KNNImputer(n_neighbors=2) 
    columns_to_impute = ['price']
    calendar[columns_to_impute] = imputer.fit_transform(calendar[columns_to_impute])

    #------------------------Reviews----------------------
    reviews = pd.read_excel(path + "/Tableau Full Project.xlsx", sheet_name="Reviews")
    reviews = reviews.dropna(subset=['reviewer_id', 'comments'])

    listings.rename(columns={'id': 'listing_id'}, inplace=True)

    #------------------------Merging Datasets----------------------
    merged_data = pd.merge(listings, reviews, on='listing_id', how='left')
    final_data = pd.merge(merged_data, calendar, on='listing_id', how='left')
    print(final_data)

    return final_data
