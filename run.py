# import time
# from source.FootballDataApi import FootballDataApi
# from database.FootballDatabase import FootbalDatabase
# im = ImportData()
# db = FootbalDatabase()
# db.connect()
# API_KEY = im.getApiKey()
# api = FootballDataApi(API_KEY)

# limit = 500  # max limit
# offset = 0
# while limit <= 10000:
#     data = api.getTeams(limit, offset)
#     teams = data["teams"]
#     print(teams)
#     for team in teams:
#         db.execute("INSERT INTO Teams (Id, Name, ShortName, Tla, Crest, Address, Website, Founded, ClubColors, Venue, LastUpdated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
#                    (team["id"], team["name"], team["shortName"], team["tla"], team["crest"], team["address"], team["website"], team["founded"], team["clubColors"], team["venue"], team["lastUpdated"]))
#     offset = offset + 500
#     limit = limit + 500
#     time.sleep(6)  # max 10 calls/min
