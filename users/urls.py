

from users.views import *
from django.urls import path,include


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("oauth/", include("social_django.urls")),
    path("register/", register, name="register"),
    
]