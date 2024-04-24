from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions
from ApiApp.models import Product
from .serializers import ProductSerializer
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json




class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # permission_classes = [permissions.IsAuthenticated]


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     # user can only update, delete own posts
    #     return Product.objects.filter(user=user)
    
# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         try:
#             data = JSONParser().parse(request)  # data is a dictionary
#             user = User.objects.create_user(username=data['username'], password=data['password'])
#             user.save()
#             token = Token.objects.create(user=user)
#             return JsonResponse({'token': str(token)}, status=201)
#         except IntegrityError:
#             return JsonResponse({'error': 'Username taken. Choose another username.'}, status=400)

# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         username = data.get('username', None)
#         password = data.get('password', None)

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             token, _ = Token.objects.get_or_create(user=user)
#             return JsonResponse({'token': token.key}, status=200)
#         else:
#             return JsonResponse({'error': 'Invalid credentials'}, status=400)