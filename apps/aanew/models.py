from django.db import models

class Link(models.Model):

    title = models.CharField(max_length=100, unique=True)
    url = models.URLField()
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.url)

class LinkAdded(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    link = models.ForeignKey(Link)
    session_key = models.CharField(max_length=100)
    flags = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.link)

class LinkFollowed(models.Model):
    link = models.ForeignKey(Link)
    when = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.link)
