import requests as rq


class FootballDataApi:
    BASE_URL = 'http://api.football-data.org/v4'

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'X-Auth-Token': self.api_key
        }

    def _get(self, endpoint, params=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = rq.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(
                f"Error: {response.status_code} - {response.text}.\nEndpoint: {url}")

    def getPersons(self, playerId):
        endpoint = f"/persons/{str(playerId)}"
        return self._get(endpoint)

    def getCompetitions(self, competition):
        endpoint = f"/competitions/{competition}"
        return self._get(endpoint)

    def getAreas(self):
        endpoint = f"/areas"
        return self._get(endpoint)

    def getTeams(self, limit=0, offset=0):
        if limit > 0:
            endpoint = f"/teams?limit={limit}&offset={offset}"
        else:
            endpoint = f"/teams"
        return self._get(endpoint)
