from django.urls import path

from . import views
from .views import JobView, JobWithIdView, login_user, register
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


urlpatterns = [
    path("job/", csrf_exempt(JobView.as_view()) , name="job_view"),
    path("job/<int:pk>/", csrf_exempt(JobWithIdView.as_view()) , name="job_with_id_view"),
    path('register/', csrf_exempt(register), name='register'),
    path('login/',  csrf_exempt(login_user), name='login_user'),
]