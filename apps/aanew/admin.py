from django.contrib import admin

from aanew.models import Link, LinkAdded, LinkFollowed

admin.site.register(Link)

def title(link_added): return link_added.link.title
def URL(link_added): return link_added.link.url
def when(link_added): return link_added.added
class LinkAddedAdmin(admin.ModelAdmin):
    list_display = (title, URL, when, 'flags')
admin.site.register(LinkAdded, LinkAddedAdmin)

def when(link_followed): return link_followed.when
def follow_count(link_followed): return link_followed.link.linkfollowed_set.count()
class LinkFollowedAdmin(admin.ModelAdmin):
    list_display = (URL, follow_count, when, 'session_key')
admin.site.register(LinkFollowed, LinkFollowedAdmin)
