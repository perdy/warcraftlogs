from requests import Session
from urllib import parse

from warcraftlogs.models import Zone, Class
from warcraftlogs.models.rankings import Fight


class WarcraftLogsClient:
    HOST = 'https://www.warcraftlogs.com/v1/'

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = Session()

    def _get(self, path, **kwargs):
        params = {'api_key': self.api_key}
        params.update(kwargs)

        url = parse.urljoin(self.HOST, path)

        return self.session.get(url, params=params)

    def zones(self):
        return [Zone.from_dict(z) for z in self._get('zones').json()]

    def classes(self):
        return [Class.from_dict(c) for c in self._get('classes').json()]

    def rankings_encounter(self, encounter_id, **params):
        path = 'rankings/encounter/{}'.format(encounter_id)
        return [Fight.from_dict(f, encounter=encounter_id) for f in self._get(path, **params).json()['rankings']]

    def rankings_character(self, name, server, region, **params):
        path = 'rankings/character/{}/{}/{}'.format(name, server, region)
        return [Fight.from_dict(f, name=name, server=server, region=region) for f in self._get(path, **params).json()]
