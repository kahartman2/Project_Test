import pandas as pd

records = pd.read_csv('mich_restaurants_2019.csv')
mich_dict = records.to_dict('records')

records2 = pd.read_csv('nyc_zipcodes.csv')
zip_dict = records2.to_dict('records2')

records3 = pd.read_csv('geocode2.csv')
address_dict = records3.to_dict('records3')
