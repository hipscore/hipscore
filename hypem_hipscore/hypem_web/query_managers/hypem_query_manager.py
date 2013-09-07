import requests


class HypemQueryManager(object):
    USER_ENDPOINT = "http://hypem.com/playlist/loved/%(username)s/json/%(offset)s/data.js"
    
    def _query(self,endpoint):
        result = {}
        try:
            res = requests.get(endpoint)
            result = res.json()
        except requests.exceptions.RequestException as e:
            pass
            
        return result

    def get_favorites(self,username,offset=1):
        endpoint = self.USER_ENDPOINT % {'username':username,
                                         'offset':1}
        return self._query(endpoint)

hypem_manager = HypemQueryManager()
