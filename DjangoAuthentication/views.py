from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from loginDjangoApp.serializers import UserSerializer

# Create your views here.


@api_view(["POST"])
def user_registration(request):
    data = request.data
    username = data["username"]
    email = data["email"]
    password = data["password"]

    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    return Response({"message": "Data Saved Successfully"})


@api_view(["POST"])
def oauth_login(request):
    data = request.data
    username = data["username"]
    password = data["password"]

    # to authentictae user we use authenticate() method
    user = authenticate(username=username, password=password)
    # if user.is_active:
    #     print("User is valid, active and authenticated")

    if user is not None:
        login(request, user)
        return Response(
            {"message": "Login Successfull", "user": UserSerializer(user).data}
        )
    else:
        return Response({"message": "Invalid Credentials"})


@api_view(["GET"])
def getUsers(request):
    users = User.objects.all()
    usersList = []
    for user in users:
        usersList.append(UserSerializer(user).data)

    return Response({"users": usersList})


@api_view(["GET"])
def getLoggedInUser(request):
    if request.user.is_authenticated:
        return Response({"user": UserSerializer(request.user).data})
    else:
        return Response({"message": "User is not logged in"})

@api_view(["GET"])
def logout_user(request):
    logout(request)
    return Response({"message": "Logout Successfull"})
