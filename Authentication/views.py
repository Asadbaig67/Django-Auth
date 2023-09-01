from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Custom_User
from loginDjangoApp.serializers import RegisterSerializer
from django.contrib.auth import authenticate, login

# Create your views here.


# USER REGISTERATION API
@api_view(["POST"])
def registration(request):
    data = request.data
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data Saved Successfully"})
    return Response(serializer.errors)


# USER LOGIN API
@api_view(["POST"])
def user_login(request):
    data = request.data
    email = data["email"]
    password = data["password"]

    # to authentictae user we use authenticate() method
    # user = authenticate(email=email, password=password)

    user = Custom_User.objects.get(email=email)
    serialized_user = RegisterSerializer(user)
    if serialized_user is not None:
        if serialized_user.data["password"] == password:
            request.session["email"] = serialized_user.data["email"]
            email = request.session.get("email")
            print(email)
            # to login user we use login() method which takes request and user as parameter and logs in the user for the session
            return Response(
                {"message": "Login Successfull", "Custom_User": serialized_user.data}
            )
    else:
        return Response({"message": "Invalid Credentials", "Custom_User": None})


# GET ALL USERS API
@api_view(["GET"])
def getData(request):
    data = Custom_User.objects.all()
    serializer = RegisterSerializer(data, many=True)  # Serialize the queryset
    return Response({"message": "Data Fetched Successfully", "data": serializer.data})


def home(request):
    return HttpResponse("Hello World")


@api_view(["GET"])
def getloggedinUser(request):
    email = request.session.get("email")
    print(email)
    if email is not None:
        return Response({"message": "Logged In Users Email Is", "email": email})
    else:
        return Response({"message": "No Custom_User Logged In", "email": None})
