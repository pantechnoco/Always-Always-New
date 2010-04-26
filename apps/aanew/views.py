from urlparse import urlparse

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from aanew.models import Link, LinkAdded, LinkFollowed

def submit_link(request):
    new_url = request.GET.get('new_url', None)

    if urlparse(new_url).scheme in ('http', 'https'):
        title = request.GET.get('title', None)
        link, new = Link.objects.get_or_create(url=new_url, defaults={
            'title': title, 
        })

        flags = request.GET.get('flags', '')
        LinkAdded.objects.create(session_key=request.session.session_key, link=link, flags=flags)

        request.session['just_added'] = str(link.id)
        
        return_to = '/'

    else:
        return_to = '/?error=scheme'

    return HttpResponseRedirect(return_to)

def follow_link(request, link_id):
    try:
        link = Link.objects.get(id=link_id)
    except Link.DoesNotExist:
        redirect_url = '/?error=badfollow&error-linkid=%d' % (link_id,)
    except:
        redirect_url = '/?error=unknown'
    else:
        redirect_url = link.url
        LinkFollowed.objects.create(link=link, session_key=request.session.session_key)
    return HttpResponseRedirect(redirect_url)
    

def list_links(request):
    links = Link.objects.all().order_by('-linkadded__added')
    try:
        just_added = int(request.session['just_added'])
    except (ValueError, KeyError):
        just_added = None
    request.session['just_added'] = ''

    return render_to_response("aanew/list.html",
        RequestContext(request, {
            'links': links,
            'just_added': just_added,
        }))

