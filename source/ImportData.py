from source.FootballDataApi import FootballDataApi
from database.FootballDatabase import FootbalDatabase
import time


class ImportData:
    def __init__(self):
        self.db = FootbalDatabase()
        self.db.connect()
        self.API_KEY = self.getApiKey()
        self.api = FootballDataApi(self.API_KEY)

    def importAreasToDb(self):
        try:
            data = self.api.getAreas()
            areas = data["areas"]

            for area in areas:
                self.db.execute("INSERT INTO Areas (Id, AreaName, CountryCode, Flag, ParentAreaId, ParentAreaName) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
                                (area["id"], area["name"], area["countryCode"], area["flag"], area["parentAreaId"], area["parentArea"]))
            print("Areas imported")
        except Exception as e:
            print(f"Areas import failed: {e}")
            raise

    def getApiKey(self):
        self.db.cursor.execute(
            "SELECT KeyValue FROM Keys WHERE KeyName = 'FootballData' LIMIT 1")
        result = self.db.fetchone()
        return result[0]

    def importTeams(self):
        try:
            limit = 500  # max limit
            offset = 0
            while limit <= 10000:
                data = self.api.getTeams(limit, offset)
                teams = data["teams"]
                for team in teams:
                    self.db.execute("INSERT INTO Teams (Id, Name, ShortName, Tla, Crest, Address, Website, Founded, ClubColors, Venue, LastUpdated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
                                    (team["id"], team["name"], team["shortName"], team["tla"], team["crest"], team["address"], team["website"], team["founded"], team["clubColors"], team["venue"], team["lastUpdated"]))
                offset = offset + 500
                limit = limit + 500
                time.sleep(6)  # max 10 calls/min
            print("Teams imported")
        except Exception as e:
            print(f"Teams import failed: {e}")
            raise
