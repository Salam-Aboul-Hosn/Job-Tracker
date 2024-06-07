from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from .models import Job

class JobView(View):
    def get(self, request):
        return HttpResponse("Hello, world. This is a get request")

    def post(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. This is a post request.")
        

    def patch(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. This is a patch request")


    def delete(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. This is a delete request")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")