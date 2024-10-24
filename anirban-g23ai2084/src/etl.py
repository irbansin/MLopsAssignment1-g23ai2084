import mysql.connector

connection = mysql.connector.connect(
    host='34.93.188.48]',  # Replace with your instance IP
    user='airbnb-master',             # Replace with your DB username
    password='gruntoxy007',         # Replace with your DB password
    database='postgres'            # Replace with your database name
)
cursor = connection.cursor()