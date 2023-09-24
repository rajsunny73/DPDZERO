from django.shortcuts import render
from .serializers import RegisterSerializers,TokenSerializers,StorageSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RegisterModels,TokenModels,StorageModels
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token 


# Create your views here.
class Register(APIView):
    def get(self, request):
        register=RegisterModels.objects.all()
    
        serializer_class=RegisterSerializers(register,many=True)
        return Response(serializer_class.data)
    
    def post(self, request):
        serializer = RegisterSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            successResponse={"status": "success",
            "message": "User successfully registered!",
             "data":serializer.data }
            
            return Response(successResponse, status=status.HTTP_200_OK)
        errorResponse={
            "status": "error",
            "code": "INVALID_REQUEST",
            "message": "Invalid request. Please provide all required fields: username, email, password, full_name."
        }
        return Response(errorResponse, status=status.HTTP_400_BAD_REQUEST)
    

class TokenResponse(APIView):
    def get(self, request):
        token=TokenModels.objects.all()
  
        serializer_class=TokenSerializers(token,many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer = TokenSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=serializer.validated_data['userName']
            token,created=Token.objects.get_or_create(user=user)
            successResponse={"status": "success",
            "message":"Access token generated successfully.",
                "data": {
                "access_token": token.key,
                "expires_in": 3600
                }}
            return Response(successResponse, status=status.HTTP_200_OK)
        errorResponse={
            "status": "error",
            "code": "INVALID_REQUEST",
            "message": "INVALID_CREDENTIALS"
        }
        return Response(errorResponse, status=status.HTTP_400_BAD_REQUEST)
    
    
class Storage(APIView):
        def get(self, request,pk=None):
            if pk:
                storage=StorageModels.objects.filter(key=pk)
                serializer_class=StorageSerializers(storage,many=True)
                successResponse={
                        "status": "success",
                        "data": serializer_class.data}
                return Response(successResponse)
                    
            else:
                storage=StorageModels.objects.all()
                serializer_class=StorageSerializers(storage,many=True)
                return Response(serializer_class.data)

        def post(self, request):
            serializer = StorageSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                successResponse={"status": "success",
                "message": "Data stored Sucessfully!!",
                }
                return Response(successResponse, status=status.HTTP_200_OK)
            errorResponse={
                "status": "error",
                "code": "INVALID_REQUEST",
                "message": "INVALID_CREDENTIALS"
            }
            return Response(errorResponse, status=status.HTTP_400_BAD_REQUEST)
        
        def put(self, request, pk=None, format=None):
            student = StorageModels.objects.filter(key=pk).first()
            student_serializers = StorageSerializers(instance=student, data=request.data)
            if student_serializers.is_valid():
                student_serializers.save()
                successResponse={"status": "success",
                    "message": "Updated Sucessfully!!",
                    "data":student_serializers.data }
                return Response(successResponse, status=status.HTTP_200_OK)
            return Response(student_serializers.data, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self,request, pk=None,):
            student = StorageModels.objects.filter(key=pk)
            student.delete()
            return Response({"status": "success",
                        "message": "Data deleted successfully."
                        }, status=status.HTTP_204_NO_CONTENT)