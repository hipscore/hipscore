from django.db import models

# Create your models here.
class HypemTrack(models.Model):

    #hypem fields
    mediaia = models.CharField(max_length=63)
    artist = models.CharField(max_length=127)
    title = models.CharField(max_length=127)
    dateposted = models.DateTimeField()
    description = models.TextField()
    thumb_url = models.URLField()
