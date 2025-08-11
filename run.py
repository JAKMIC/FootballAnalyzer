from source.FootballDataApi import FootballDataApi
from database.FootballDatabase import FootbalDatabase

API_KEY = 'a6f3fb2782994d2ca1e02bfa032c6566'
api = FootballDataApi(API_KEY)

db = FootbalDatabase()
db.connect()

data = api.getAreas()
areas = data["areas"]

for area in areas:
    db.execute("INSERT INTO Areas (Id, AreaName, CountryCode, Flag, ParentAreaId, ParentAreaName) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
               (area["id"], area["name"], area["countryCode"], area["flag"], area["parentAreaId"], area["parentArea"]))
