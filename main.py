import requests

aapl = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&outputsize=full&apikey=AKIBVM0JT94E6ST7' #api call for apple data

ibm = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=AKIBVM0JT94E6ST7' #api call for ibm data (30 days)

aapl_out = requests.get(aapl)
aapl_data = aapl_out.json()

ibm_out = requests.get(ibm)
ibm_data = ibm_out.json()

print(aapl_data)
print("--------------------------------------------")
print(ibm_data)


