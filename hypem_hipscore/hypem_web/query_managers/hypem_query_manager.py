import requests
import datetime
from hypem_web.models import HypemTrack


class HypemQueryManager(object):

    FAVORITES_ENDPOINT = "http://hypem.com/playlist/loved/%(username)s/json/%(offset)s/data.js"
    POPULAR_ENDPOINT = "http://hypem.com/playlist/popular/3day/json/%(offset)s/data.js"
    USER_ENDPOINT = "http://api.hypem.com/api/get_profile?username=%(username)s"
    TIMEMACHINE_ENDPOINT = "http://localhost:3000/popular/%(date)s/"
    TRACKSOURCE_ENDPOINT = "http://localhost:3000/source/%(track_media_id)s/"

    def _query(self,endpoint):
        result = {}
        try:
            res = requests.get(endpoint)
            result = res.json()
        except requests.exceptions.RequestException as e:
            pass
            
        return result

    def get_track_source(self,track_media_id):
        endpoint = self.TRACKSOURCE_ENDPOINT % {'track_media_id':track_media_id}
        res = requests.get(endpoint)
        return res.json()

    def get_favorites(self,username,offset=1):
        endpoint = self.FAVORITES_ENDPOINT % {'username':username,
                                              'offset':offset}
        res = requests.get(endpoint)
        json_data = res.json()
        del json_data['version']
        return json_data.values()

    def get_timemachine(self,date):
        date_str = date.strftime("%b-%d-%Y")
        endpoint = self.TIMEMACHINE_ENDPOINT % {'date':date_str}
        res = requests.get(endpoint)
        return res.json()

    def get_popular(self,offset=1):
        endpoint = self.POPULAR_ENDPOINT % {'offset':offset}
        res = requests.get(endpoint)
        json_data = res.json()
        del json_data['version']
        return json_data.values()

    def get_user(self,username):
        endpoint = self.USER_ENDPOINT % {'username':username}
        res = requests.get(endpoint)
        return res.json()

    def _parse_track_data(self,raw_track_data):
        #hack to get rid of version stuff
        del raw_track_data['version']

        media_ids = [track['mediaid'] for track in raw_track_data.values()]
        known_tracks_map = dict([(track.mediaid,track) for track in HypemTrack.objects.filter(mediaid__in=media_ids)])

        tracks_result = []
        #Get Models Associated with Raw Data
        for playlist_num,track_data in raw_track_data.items():
            if track_data['mediaid'] in known_tracks_map:
                track = known_tracks_map[track_data['mediaid']]
            else:
                track = HypemTrack(
                    mediaid=track_data['mediaid'],
                    artist=track_data['artist'],
                    title=track_data['title'],
                    dateposted=datetime.datetime.fromtimestamp(track_data['dateposted']),
                    description=track_data['description'],
                    thumb_url=track_data['thumb_url']
                )
                track.save()
                known_tracks_map[track.mediaid] = track

            tracks_result.append(track)

        
                
        return tracks_result


hypem_manager = HypemQueryManager()
