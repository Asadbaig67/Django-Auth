from django.urls import path
from .views import *

urlpatterns = [
    path("user/registration/", user_registration, name="user_registration"),
    path("user/oauth_login/", oauth_login, name="oauth_login"),
    path("user/get-users/", getUsers, name="getUsers"),
    path("user/logout/", logout_user, name="logout_user"),
    path("user/get-logged-in-user/", getLoggedInUser, name="getLoggedInUser"),
]
