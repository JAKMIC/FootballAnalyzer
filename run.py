from source.FootballDataApi import FootballDataApi
import pandas as pd

# import requests as rq
# url = "http://api.football-data.org/v4/competitions"
# response = rq.get(url)
# print(response.json())

API_KEY = 'a6f3fb2782994d2ca1e02bfa032c6566'
api = FootballDataApi(API_KEY)
person = api.getPersons(44)

df = pd.json_normalize(person)
print(df.head())
