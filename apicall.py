# python api call
# https://www.eia.gov/opendata/browser/petroleum/pri/gnd?frequency=weekly&data=value;&sortColumn=period;&sortDirection=desc;
# importing the requests library
import requests
import constants
import json
import csv
csv_file_path = 'gas_prices.csv'

# api-endpoint
URL = "https://api.eia.gov/v2/petroleum/pri/gnd/data/?frequency=weekly&data[0]=value&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000&api_key=" + constants.API_KEY

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
response = r.json()

API_Data = response["response"]["data"]
keys = API_Data[0].keys()

for price in API_Data:
    print(price)

with open(csv_file_path, mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    # Write data to the CSV file
    writer.writerows(keys)
