from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return str(self.name)


class User(models.Model):
    uiid = models.CharField(max_length=1000, blank=True, null=True, unique=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    picture = models.ImageField(upload_to='user_pictures', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return str(self.nickname)