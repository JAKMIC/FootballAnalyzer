from source.FootballDataApi import FootballDataApi
from database.FootballDatabase import FootbalDatabase


class ImportData:
    def __init__(self):
        self.API_KEY = 'a6f3fb2782994d2ca1e02bfa032c6566'
        self.api = FootballDataApi(self.API_KEY)
        self.db = FootbalDatabase()
        self.db.connect()

    def importAreasToDb(self):
        data = self.api.getAreas()
        areas = data["areas"]

        for area in areas:
            self.db.execute("INSERT INTO Areas (Id, AreaName, CountryCode, Flag, ParentAreaId, ParentAreaName) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
                            (area["id"], area["name"], area["countryCode"], area["flag"], area["parentAreaId"], area["parentArea"]))
