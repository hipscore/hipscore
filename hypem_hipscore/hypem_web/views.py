from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import json

from hypem_web.query_managers import hypem_manager

def index(request):
    return render_to_response("index.html",{},RequestContext(request))

def favorites(request,username):
    offset = request.GET.get("offset",1)
    favorites = hypem_manager.get_favorites(username,offset)
    return HttpResponse(json.dumps(favorites),content_type="application/json")
