from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core import serializers
import json

from hypem_web.query_managers import hypem_manager

def index(request):
    return render_to_response("index.html",{},RequestContext(request))

def favorites(request,username):
    offset = request.GET.get("offset",1)
    hypem_tracks_json = hypem_manager.get_favorites(username,offset)

    return HttpResponse(json.dumps(hypem_tracks_json),
                        content_type="application/json")

def user(request,username):
    hypem_user_json = hypem_manager.get_user(username)

    return HttpResponse(json.dumps(hypem_user_json),
                        content_type="application/json")

def popular(request):
    offset = request.GET.get("offset",1)
    hypem_tracks_json = hypem_manager.get_popular(offset)
    return HttpResponse(json.dumps(hypem_tracks_json),
                        content_type="application/json")
