from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
import ast
from rest_framework import status


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    SessionAuthentication scheme used by DRF. DRF's SessionAuthentication uses
    Django's session framework for authentication which requires CSRF to be
    checked. In this case we are going to disable CSRF tokens for the API.
    """

    def enforce_csrf(self, request):
        return


@permission_classes((AllowAny,))
class SignUpViewset(viewsets.ViewSet):
    """
    A simple ViewSet for sign up
    """

    def list(self, request):
        queryset = []
        target = self.request.query_params.get("target", None)
        if target is not None:
            queryset = CustomUser.objects.filter(id=target)
            serializer = CustomUserSerializer(queryset, many=True)
            return Response(serializer.data)
        return Response({"message": "succes"})

    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.filter(id=pk)
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data
        )
    def create(self, request, *args, **kwargs):
        flag = request.data["flag"]
        username = request.data["username"]
        password = request.data["password"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        contact = request.data["contact"]
        if flag == str(1):
            user = CustomUser(
                username= username,
                password = password,
                first_name=first_name,
                last_name = last_name,
                contact = contact
            )
            user.save()
            serializer = CustomUserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)

        # handle modification here
        if flag == str(0):
            user_id = request.data["id"]
            user = CustomUser.objects.filter(id=user_id);
            if(len(user)>0):
                myuser = user[0]
                myuser.username= username
                myuser.password = password
                myuser.first_name=first_name
                myuser.last_name = last_name
                myuser.contact = contact
                myuser.save()
            else:
                return Response({"message": "fail"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            pass
        except:
            return Response("", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "succes"},status=status.HTTP_201_CREATED)
@permission_classes((AllowAny,))
class ForfaitViewset(viewsets.ViewSet):
    """
    A simple ViewSet for forfait
    """

    def list(self, request):
        queryset = []
        # target = self.request.query_params.get("target", None)
        queryset = Forfait.objects.all()
        serializer = ForfaitSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.filter(id=pk)
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data
        )
    def create(self, request, *args, **kwargs):
        date = request.data["date"]
        offer = request.data["offer"]
        price = request.data["price"]
        quantity = request.data["quantity"]
        active = request.data["active"]
        expiry_date = request.data["expiry_date"]
        user_id = request.data["id"]
        try:
           user = CustomUser.objects.get(id=user_id)
        except :
           user = None
        finally:
            if user is not None:
                forfait = Forfait(
                   user = user,
                   date = date,
                   expiry_date=expiry_date,
                   active=active,
                   offer =offer,
                   price = price,
                   quantity =quantity
                )
                forfait.save()

        

        return Response({"message": "succes"})