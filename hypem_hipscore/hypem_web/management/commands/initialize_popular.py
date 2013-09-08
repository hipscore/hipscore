from django.core.management.base import BaseCommand, CommandError
import datetime
from hypem_web.query_managers import hypem_manager
from hypem_web.models import (HypemPopularSnapshot,
                              HypemTrack,
                              HypemRankListing)



class Command(BaseCommand):
    def handle(self, *args, **options):

        start_date = datetime.date(year=2013,month=4,day=1)
        end_date = datetime.date(year=2013,month=8,day=26)
        date_diff = datetime.timedelta(days=7)

        cur_date = start_date
        
        known_tracks_map = dict([(track.mediaid,track) for track in HypemTrack.objects.all()])

        while cur_date < end_date:
            snapshot = HypemPopularSnapshot(date=cur_date)
            snapshot.save()
            
            popular_tracks_data = hypem_manager.get_timemachine(date=cur_date)['tracks']
            for track_data in popular_tracks_data:
                rank = popular_tracks_data.index(track_data)+1
                if known_tracks_map.has_key(track_data['id']):
                    track = known_tracks_map[track_data['id']]
                else:
                    track = HypemTrack(
                        mediaid=track_data['id'],
                        artist=track_data['artist'],
                        title=track_data['song'],
                    )
                    track.save()
                    known_tracks_map[track.mediaid] = track
                        
                rank_listing = HypemRankListing(hypemtrack=track,
                                                hypempopularsnapshot=snapshot,
                                                rank=rank)
                rank_listing.save()

            cur_date+=date_diff
