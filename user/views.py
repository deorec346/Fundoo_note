import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.response import Response
from .models import User


# Create your views here.

def user_registration(request):

    """
           this method is use for user Registration
           :param request: user_details
           :return:response
    """

    try:
        if request.method == "POST":
            register = json.loads(request.body)
            print(register)
            u = User.objects.create(name=register.get('name'), password=register.get('password'), email_id=register.get('email_id'), phone=register.get('phone'),age=register.get('age'),location=register.get('location'))
            print(u)
            u.save()

            return JsonResponse({
                'message': 'User added successfully'
            })
    except Exception as e:
        print(e)
        return JsonResponse({
            'message': 'User not there or enter proper registration details'
        })


def user_login(request):

    """
      this method is use for user login
      :param request: username and password
      :return:response
    """

    try:
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if user is not None:
            return Response({"message": "successfully login"})
        else:
            return Response({"message": "login error"})
    except Exception as e:
        return Response({"message": str(e)})