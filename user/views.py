from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializers

# Create your views here.
class CustomUserCreateAPIView(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        user = CustomUser.objects.all()
        serializer = UserSerializers(user, many=True)
        return Response({"list":serializer.data, "message":'success'}, status=status.HTTP_200_OK)

class CustomUserDetailAPIView(APIView):
    def object_data(self, id):
        try:
            return CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return None
        
    def get(self, request, id):
        user = self.object_data(id)
        if not user:
            return Response({"error":"user not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializers(user)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)  
    
    def put(self, request, id):
        user = self.object_data(id)
        if not user:
            return Response({'error':"user not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializers(user, data=request.data, partial=True) # partial=True => patch like update
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "message":"success"}, status=status.HTTP_200_OK)
        return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        user = self.object_data(id)       
        if not user:
            return Response({"error":"user not found"}, status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response({"message":"User Deleted", "status":"success"}, status=status.HTTP_200_OK)
        
          