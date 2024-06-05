import pandas as pd

df = pd.read_csv('yellow_tripdata_2019-01.csv', nrows=100)

# print(df)

pd.io.sql.get_schema(df, name='yellow_taxi_data')