from source.FootballDataApi import FootballDataApi
from database.FootballDatabase import FootbalDatabase


class ImportData:
    def __init__(self):
        self.db = FootbalDatabase()
        self.db.connect()
        self.API_KEY = self.getApiKey()
        self.api = FootballDataApi(self.API_KEY)

    def importAreasToDb(self):
        data = self.api.getAreas()
        areas = data["areas"]

        for area in areas:
            self.db.execute("INSERT INTO Areas (Id, AreaName, CountryCode, Flag, ParentAreaId, ParentAreaName) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
                            (area["id"], area["name"], area["countryCode"], area["flag"], area["parentAreaId"], area["parentArea"]))

    def getApiKey(self):
        self.db.cursor.execute(
            "SELECT KeyValue FROM Keys WHERE KeyName = 'FootballData' LIMIT 1")
        result = self.db.fetchone()
        return result[0]
