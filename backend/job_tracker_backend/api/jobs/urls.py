from django.urls import path

from . import views
from .views import JobView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

urlpatterns = [
    path("job/", csrf_exempt(JobView.as_view()) , name="job_view"),
]