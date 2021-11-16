from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import*
from .serializers import*
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView






from rest_framework import generics
class studentgeneric(generics.ListCreateAPIView,generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = studentserializers

class studentgeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = studentserializers
    lookup_field='id'
class generratepdf(APIView):
    def get(self,request):
        return Response({'status':200})

""" @api_view(['GET'])
def home(request):
    student_obj=student.objects.all()
    serializer=studentserializers(student_obj,many=True)

    return Response({"message": "Hello, world!",'playload':serializer.data})
@api_view(['POST'])
def post_student(request):
    data=request.data
    serializer=studentserializers(data=request.data)
    if not  serializer.is_valid():
        print(serializer.errors)
        return  Response({"status":403,'errors':serializer.errors,"message": "something is wrong"})
    serializer.save() 
    return Response({'status':200,"message": "Hello, your data is saved",'payload':data})

@api_view(['PATCH'])
def update_student(request,id):
    try:
        student_obj=student.objects.get(id=id)
        serializer=studentserializers(student_obj,data=request.data,partial=True)
        if not  serializer.is_valid():
           print(serializer.errors)
           return  Response({"status":403,'errors':serializer.errors,"message": "something is wrong"})
        serializer.save() 
        return Response({'status':200,"message": "Hello, your data is saved",'payload':serializer.data})  
    except Exception as e:
        print(e)
        return Response({'student':403,'message':'invalid   id'})

@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student_obj=student.objects.get(id=id)
        student_obj.delete()
        return Response({"status":200,"message":"deleted"})


    except Exception as e:
        print(e)
        return Response({"status":404,"message":'invalid id'}) """
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication        
class studentapi(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        student_obj=student.objects.all()
        serializer=studentserializers(student_obj,many=True)
        print(request.user)
        return Response({"message": "Hello, world!",'playload':serializer.data})
    def post(self,request):
        data=request.data
        serializer=studentserializers(data=request.data)
        if not  serializer.is_valid():
          print(serializer.errors)
          return  Response({"status":403,'errors':serializer.errors,"message": "something is wrong"})
        serializer.save() 
        return Response({'status':200,"message": "Hello, your data is saved",'payload':data})

    def put(self,request):
        try:
           student_obj=student.objects.get(id=request.data['id'])
           serializer=studentserializers(student_obj,data=request.data,partial=False)
           if not  serializer.is_valid():
              print(serializer.errors)
              return  Response({"status":403,'errors':serializer.errors,"message": "something is wrong"})
           serializer.save() 
           return Response({'status':200,"message": "Hello, your data is saved",'payload':serializer.data})  
        except Exception as e:
           print(e)
           return Response({'student':403,'message':'invalid   id'})
    def patch(self,request):
        try:
           student_obj=student.objects.get(id=request.data['id'])
           serializer=studentserializers(student_obj,data=request.data,partial=True)
           if not  serializer.is_valid():
              print(serializer.errors)
              return  Response({"status":403,'errors':serializer.errors,"message": "something is wrong"})
           serializer.save() 
           return Response({'status':200,"message": "Hello, your data is saved",'payload':serializer.data})  
        except Exception as e:
           print(e)
           return Response({'student':403,'message':'invalid   id'})
    def delete(self,request):
        try:
            student_obj=student.objects.get(id=request.data['id'])
            student_obj.delete()
            return Response({"status":200,"message":"deleted"})


        except Exception as e:
           print(e)
           return Response({"status":404,"message":'invalid id'})










@api_view(['GET'])
def get_book(request):
    book_obj=book.objects.all()
    serializer=bookserializer(book_obj,many=True)
    return Response({'status':200,'playload':serializer.data})
from rest_framework_simplejwt.tokens import RefreshToken       
class RegisterUser(APIView):
    def post(self,request):
        data=request.data
        serializer= userserializers(data=request.data) 
        if not  serializer.is_valid():
            print(serializer.errors)
            return  Response({"status":403,'errors':serializer.errors,"message": "something is wrong"})
        serializer.save() 
        user=User.objects.get(username=serializer.data['username'])
        #token_obj,_=Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)
        return Response({'status':200,'refresh': str(refresh),
        'access': str(refresh.access_token),"message": "Hello, your data is saved",'payload':data})
      