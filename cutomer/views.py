from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializers, CustomerResetPass, CustomerForgotPass
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.
class CustomerCreateAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serialize = CustomerSerializers(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"data":serialize.data, 'status':'success'},status=status.HTTP_200_OK)
        first_error = next(iter(serialize.errors.values()))[0]
        return Response({"error": first_error}, status=status.HTTP_400_BAD_REQUEST)
        
   
class CustomerResetAPIView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        password=request.data.get('password')
        print('password3', password)
        try:
            customer = Customer.objects.get(email = email)
        except:
            return Response({'error':'email not found'},status=status.HTTP_400_BAD_REQUEST)  
        
        try:
          password_ = check_password(password, customer.password)
          print(password_,"vccc")
          if password_:
            serializer = CustomerResetPass(customer,data=request.data)
            if serializer.is_valid():
             serializer.save()
             return Response({"message":"Password rest success"}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
          else :
              return Response({"error":'old pass mismatch'}, status=status.HTTP_400_BAD_REQUEST) 
        except:
            return Response({"error":'invalid'}, status=status.HTTP_400_BAD_REQUEST) 
        
        # if not check_password(password, customer. password):
        #     return Response({"error":'old pass mismatch'}, status=status.HTTP_400)
   
class CustomerForgotAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            user = Customer.objects.get(email = email)
            if user:
             serializer = CustomerForgotPass(user, data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response({'message':"password reseted"}, status=status.HTTP_200_OK)
             else:
                 return Response({'error':"user not found"}) 
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                
        except:
            return Response({'error':'invalid'}, status=status.HTTP_400_BAD_REQUEST)              

class CustomerLoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            customer = Customer.objects.get(email=email)
            print('customer', customer)
        except Customer.DoesNotExist:
            return Response({'error':'user not found'}, status=status.HTTP_400_BAD_REQUEST)
        if not check_password(password,customer.password):
            return Response({'error':'password wrong'}, status=status.HTTP_400_BAD_REQUEST)
        if customer:
            user ,_= User.objects.get_or_create(email=email)  
            print('customer', customer)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'status':'success',
                'token': token.key,  
                'customer':{
                    'name':customer.name,
                    'email':customer.email,
                    'mobile':customer.mobile
                },
            },status=status.HTTP_200_OK)
        else:
            return Response({'error':'email or password failed'}, status=status.HTTP_400_BAD_REQUEST)   
