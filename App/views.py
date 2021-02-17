from django.shortcuts import render, get_object_or_404
from .models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets, mixins,generics,status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class PersonViewSet(viewsets.GenericViewSet,
	                mixins.ListModelMixin,
	                mixins.CreateModelMixin,
	                mixins.UpdateModelMixin,
	                mixins.RetrieveModelMixin,
	                 mixins.DestroyModelMixin):
	serializer_class = PersonSerializer
	queryset         = Person.objects.all()

    # def list(self, request):
    #     persons = Person.objects.all()
    #     serializer = PersonSerializer(persons, many = True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = PersonSerializer(data = request.data)

    #     if serializer.is_valid():
    #     	serializer.save()
    #     	return Response(serializer.data, status = status.HTTP_200_OK)
    #     else:
    #     	return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        	

    # def retrieve(self, request, pk=None):
    #     queryset = Person.objects.all()
    #     person   = get_object_or_404(queryset, pk = pk)
    #     serializer = PersonSerializer(person)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     person = Person.objects.get(pk = pk)
    #     serializer = PersonSerializer(person, data = request.data)

    #     if serializer.is_valid():
    #     	return Response(serializer.data, status = status.HTTP_200_OK)
    #     else:
    #     	return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        	

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     person = Person.objects.get(pk = pk)
    #     person.delete()
    #     return Response(status = status.HTTP_204_NO_CONTENT)

