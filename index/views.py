from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person

# Create your views here.
class PersonListCreateAPIView(APIView):
    def get(self, request):
        person = list(Person.objects.values())
        return Response(person)
    
    def post(self, request):
        data = request.data
        person = Person.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            age=data.get('age')
        )
        return Response({
            "id":person.id,
            "first_name":person.first_name,
            "lastname":person.last_name,
            "age":person.age
        },status=status.HTTP_201_CREATED)
        
        
class PersonDetailsAPIView(APIView):
      def get(self, request, id):
          try:
            person = Person.objects.get(id=id)
            print(person)
            return Response({
                "id":person.id,
                "first_name":person.first_name,
                "lastname":person.last_name,
                "age":person.age
            },status=status.HTTP_201_CREATED)  
          except Person.DoesNotExist:
              return Response({
                  "error":'User Not Found'
              },status=status.HTTP_200_OK) 

      def put(self, request, id):
          try:
              person = Person.objects.get(id=id)
              person.first_name = request.data.get("first_name", person.first_name)
              person.last_name = request.data.get("last_name", person.last_name)
              person.age = request.data.get("age", person.age)
              person.save()
              return Response({
                  "id":person.id,
                  "first_name":person.first_name,
                  "last_name":person.last_name,
                  "age":person.age,
                 "method":"PUT"
              }, status=status.HTTP_200_OK)
          except Person.DoesNotExist:
              return Response({
                  "error":"Person not found"
              },status=status.HTTP_404_NOT_FOUND)
              
      def patch(self, request, id):
         try:
             person = Person.objects.get(id=id)
             
             if "first_name" in request.data:
                 person.first_name = request.data["first_name"]
             if "last_name" in request.data:
                 person.last_name = request.data["last_name"]
             if "age" in request.data:
                 person.age = request.data["age"]
                 
             person.save()
             return Response({
                 "id":person.id,
                 "first_name":person.first_name,
                 "last_name":person.last_name,
                 "age":person.age,
                 "method":"PATCH"
             }, status=status.HTTP_200_OK)            
         
         except Person.DoesNotExist:
             return Response({
                 "error":"Person not found"
             },status=status.HTTP_404_NOT_FOUND)  
             
      def delete(self, request, id):
           try:
               person  = Person.objects.get(id=id)
               person.delete()
               return Response({
                   "message":"Delete Successfull"
               }, status=status.HTTP_200_OK)
           except Person.DoesNotExist:
               return Response({
                   "error":"Person not found"
               }, status=status.HTTP_404_NOT_FOUND)                     
        