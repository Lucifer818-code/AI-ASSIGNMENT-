import requests
import io
import pandas as pd

# specify the URL of the CSV file in Google Drive
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTjK3-3t20y0_yukyGbdKvtHfVb0PAgBckE82ZzrlLQX9cFGrLhC_9ejHsmlrTMyTgAl52rEovdzuyG/pub?gid=0&single=true&output=csv'

# send a GET request to the URL and get the response
response = requests.get(url)

# read the response content as a CSV string using the io module
csv_str = io.StringIO(response.content.decode('utf-8'))

# read the CSV string as a Pandas dataframe
df = pd.read_csv(csv_str)

# print the first 5 rows of the dataframe
print(df.head())
