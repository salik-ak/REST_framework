from rest_framework.response import Response
from django.shortcuts import render
from .serializers import UserRegister
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from api.models import CustomUser
from rest_framework.permissions import IsAuthenticated
# import jwt


# Create your views here.

class register(APIView):

    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registerd'
            data['username']=account.username
            data['email']=account.email
            data['phone']=account.phone
            data['dob']=account.dob
            # data['profile_picture']=account.profile_picture

            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors

        return Response(data)
    
class welcome(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content ={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)