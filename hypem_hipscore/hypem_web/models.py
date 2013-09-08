from django.db import models
import requests

# Create your models here.
class HypemTrack(models.Model):

    #hypem fields
    mediaid = models.CharField(max_length=63)
    artist = models.CharField(max_length=127)
    title = models.CharField(max_length=127)
    dateposted = models.DateTimeField(null=True,blank=True)

class HypemPopularSnapshot(models.Model):
    date = models.DateField()
    tracks = models.ManyToManyField(HypemTrack,through='HypemRankListing')

class HypemRankListing(models.Model):
    hypemtrack = models.ForeignKey(HypemTrack)
    hypempopularsnapshot = models.ForeignKey(HypemPopularSnapshot)
    rank = models.IntegerField()

    
