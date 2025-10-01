from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from .seializers import VendorSerializer
from .models import vendorCreatation
from rest_framework.permissions import AllowAny

# Create your views here.
class VendorCreationAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "message":"vendor saved successfully", "vendor":serializer.data},status=status.HTTP_200_OK)
        first_error = next(iter(serializer.errors.values()))[0]
        return Response({"status":"failed", "message":first_error},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        vendor = vendorCreatation.objects.all()
        serializer = VendorSerializer(vendor, many=True)
        return Response({"status":"success", "list":serializer.data}, status=status.HTTP_200_OK)
