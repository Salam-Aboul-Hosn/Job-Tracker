from django.urls import path
from .views import JobView, JobWithIdView, get_csrf_token, login_user, register
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("job/", JobView.as_view() , name="job_view"),
    path("job/<int:pk>/", csrf_exempt(JobWithIdView.as_view()) , name="job_with_id_view"),
    path('register/', register, name='register'),
    path('login/',  login_user, name='login_user'),
    path('csrf/',  get_csrf_token, name='get_csrf_token'),
]