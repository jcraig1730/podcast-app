from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')
    birthday = models.IntegerField()


class Podcast(models.Model):
    listen_id = models.TextField(max_length=60)
    rss = models.TextField(max_length=200)
    listen_podcast_id = models.TextField(max_length=60)
    itunes_id = models.IntegerField()
    title = models.TextField(max_length=200)
    host = models.TextField(max_length=200)
    audio = models.TextField(max_length=100)
    image = models.TextField(max_length=200)
    pub_date = models.DateField()
    length = models.IntegerField()


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete='CASCADE')
    listen_id = models.TextField(max_length=60)
    title = models.TextField(max_length=200)
    audio = models.TextField(max_length=100)
    description = models.TextField(max_length=300)


class FavoriteEpisode(models.Model):
    user = models.ForeignKey(Subscriber, on_delete="CASCADE")
    episode = models.ForeignKey(Episode, on_delete='CASCADE')


class FavoritePodcast(models.Model):
    user = models.ForeignKey(Subscriber, on_delete='CASCADE')
    podcast = models.ForeignKey(Podcast, on_delete='CASCADE')

