from django.shortcuts import render
from rest_framework.views import APIView
from .models import Students
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentsSerializers, StudentsSerialLogin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from django.contrib.auth.hashers import make_password,check_password


# Create your views here.
class StudentsListAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy()
        raw_password = data.get('password')
        if raw_password:
            data['password'] = make_password(raw_password)  # hash password

        serializer = StudentsSerializers(data=data)
        if serializer.is_valid():
            student = serializer.save()

            # create User table
            user, created = User.objects.get_or_create(
                username=student.name,
                defaults={"email": student.email},
            )
            if created:
                user.set_password(raw_password)  # user table la hashed
                user.save()

            token, _ = Token.objects.get_or_create(user=user)

            student_data = serializer.data.copy()

            return Response({
                "list": student_data,
                "status": "success",
                "token": token.key,
            }, status=status.HTTP_201_CREATED)

        first_error = next(iter(serializer.errors.values()))[0]
        return Response({"error": first_error}, status=status.HTTP_400_BAD_REQUEST)

class StudentsLoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            user = Students.objects.get(email=email)
        except Students.DoesNotExist:
            return Response({'error':'user not found'},status=status.HTTP_400_BAD_REQUEST)
        if not check_password(password,user.password):
            return Response({'error':'pasword found'},status=status.HTTP_400_BAD_REQUEST)
        if user:
            user,_=User.objects.get_or_create(email=email)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "status": "success",
                    "token": token.key,
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    },
                },
                status=status.HTTP_200_OK,
                )
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)    
            # return Response({'error', 'p'})  