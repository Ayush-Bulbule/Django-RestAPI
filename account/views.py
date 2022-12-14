from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializer import RegisterSerializer,LoginSerialzer
# Create your views here.

class RegisterView(APIView):

    

    def post(self, request):
        try:

            data = request.data

            serializer = RegisterSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Invalid data',
                }, status=400)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'User created successfully',
            }, status=201)


        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message': 'Something went wrong',
            },satus=status.HTTP_500_INTERNAL_SERVER_ERROR)




class LoginView(APIView):
    

    def post(self,request):
        try:
            data = request.data
            serializer = LoginSerialzer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Invalid data',
                }, status=400)

            response = serializer.get_jwt_token(data)

            return Response(response, status=200)

        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message': 'Something went wrong',
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
