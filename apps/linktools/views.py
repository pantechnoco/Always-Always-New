from urllib2 import urlopen
from lxml.html.soupparser import parse

from django.http import HttpResponse, HttpResponseBadRequest

try:
    from json import dumps
except ImportError:
    from simplejson import dumps


def title(request):
    
    url = request.GET.get('url', None)
    if url is None:
        return HttpResponseBadRequest()
    else:
        soup = parse(urlopen(url))
        title = soup.find('.//title').text

        return HttpResponse(dumps({
            'url': url,
            'title': title,
        }))
