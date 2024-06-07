from django.urls import path

from . import views
from .views import JobView

urlpatterns = [
    path("job/", JobView.as_view(), name="job_view"),
]