# python api call
# https://www.eia.gov/opendata/browser/petroleum/pri/gnd?frequency=weekly&data=value;&sortColumn=period;&sortDirection=desc;
# importing the requests library
import requests
import constants
import json
import csv

# api-endpoint
URL = "https://api.eia.gov/v2/petroleum/pri/gnd/data/?frequency=weekly&data[0]=value&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000&api_key=" + constants.API_KEY

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
response = r.json()

API_Data = response["response"]["data"]
keys = API_Data[0].keys()

# Specify the CSV file name
filename = "gas_prices.csv"

# Writing to CSV file
with open(filename, mode='w', newline='') as file:
    # Create a DictWriter object
    writer = csv.DictWriter(file, fieldnames=API_Data[0].keys())
    # Write the header
    writer.writeheader()
    # Write the data rows
    writer.writerows(API_Data)

print(f"Data successfully written to {filename}")
