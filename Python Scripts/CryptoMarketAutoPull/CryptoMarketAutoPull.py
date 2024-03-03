from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# Original Sandbox Environment: 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start': '1',
  'limit': '15',
  'convert': 'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# Create a DataFrame from the obtained data
df = pd.DataFrame(data['data'])

# Keep only relevant columns
df = df[['name', 'symbol', 'quote']]

# Extract cryptocurrency prices
df['price'] = df['quote'].apply(lambda x: x['USD']['price'])

# Drop the 'quote' column
df = df.drop('quote', axis=1)

# Add a timestamp column
df['timestamp'] = pd.to_datetime('now')

# Display the DataFrame
print("\nLatest Cryptocurrency Prices:")
print(df)
