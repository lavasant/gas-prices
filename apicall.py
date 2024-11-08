# python api call
# https://www.eia.gov/opendata/browser/petroleum/pri/gnd?frequency=weekly&data=value;&sortColumn=period;&sortDirection=desc;
# importing the requests library
import requests
import constants

# api-endpoint
URL = "https://api.eia.gov/v2/petroleum/pri/gnd/data/?frequency=weekly&data[0]=value&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000&api_key=" + constants.API_KEY

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()

print(data)
