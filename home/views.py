from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import*
from .serializers import*
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
@api_view(['GET'])
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
        return Response({"status":404,"message":'invalid id'})
@api_view(['GET'])
def get_book(request):
    book_obj=book.objects.all()
    serializer=bookserializer(book_obj,many=True)
    return Response({'status':200,'playload':serializer.data})  
class RegisterUser(APIView):
    def post(self,request):
        data=request.data
        serializer= userserializers(data=request.data) 
        if not  serializer.is_valid():
            print(serializer.errors)
            return  Response({"status":403,'errors':serializer.errors,"message": "something is wrong"})
        serializer.save() 
        user=User.objects.get(username=serializer.data['username'])
        token_obj=Token.objects.get_or_create(user=user)
        return Response({'status':200,'token':str(token_obj),"message": "Hello, your data is saved",'payload':data})
      