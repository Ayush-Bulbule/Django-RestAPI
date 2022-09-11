from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from home.models import Blog
from home.serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q

# Create your views here.

class BlogView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def get(self, request):


        try:
            blogs  = Blog.objects.filter(user=request.user)

            # Handle Search query
            if request.GET.get("search"):
                print("Search")
                search = request.GET.get("search")
                blogs = Blog.objects.filter(Q(title__icontains=search) | Q(blog_text__icontains=search))
            
            blogSerializer  = BlogSerializer(blogs, many=True)
            return Response({
                'data': blogSerializer.data,
                'message': 'Blogs fetched successfully',
            })  

        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message': 'Something went wrong',
            },satus=status.HTTP_500_INTERNAL_SERVER_ERROR)





        

    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = BlogSerializer(data=data)
            print("############")
            print(request.user)


            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Invalid data',
                }, status=400)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'Blog created successfully',
            }, status=201)


        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message': 'Something went wrong',
            },satus=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self,request):
        try:
            data = request.data

            blog = Blog.objects.get(uuid=data['uuid'])


            if request.user != blog.user:
                return Response({
                    'data':{},
                    'message': 'You are not authorized to edit this blog',
                },status=status.HTTP_401_UNAUTHORIZED)

            serializer = BlogSerializer(blog, data=data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Invalid data',
                }, status=400)
            
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'Blog updated successfully',
            }, status=200)


        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message': 'Something went wrong',
            },satus=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def delete(self,request):
        try:
            data = request.data

            blog = Blog.objects.get(uuid=data['uuid'])


            if request.user != blog.user:
                return Response({
                    'data':{},
                    'message': 'You are not authorized to delete this blog',
                },status=status.HTTP_401_UNAUTHORIZED)

            blog.delete()

            return Response({
                'data': {},
                'message': 'Blog deleted successfully',
            }, status=200)


        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message': 'Something went wrong',
            },satus=status.HTTP_500_INTERNAL_SERVER_ERROR)





