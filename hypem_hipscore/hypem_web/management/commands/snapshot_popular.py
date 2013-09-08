from django.core.management.base import BaseCommand, CommandError
from hypem_web.query_managers import hypem_manager
from hypem_web.models import (HypemPopularSnapshot,
                              HypemRankListing)

class Command(BaseCommand):
    def handle(self, *args, **options):
        snapshot = HypemPopularSnapshot()
        snapshot.save()

        popular_tracks = hypem_manager.get_popular()
        for track in popular_tracks:
            rank = popular_tracks.index(track)+1

            rank_listing = HypemRankListing(hypemtrack=track,
                                            hypempopularsnapshot=snapshot,
                                            rank=rank)
            rank_listing.save()

        

            
            

            
        
