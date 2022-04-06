from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from pokemon_api import serializers


class PokemonSpeciesView(APIView):
    """Test getting pokemon species view"""
    
    def get(self, request, format=None):
        
        pokemon_test_view = [
            'User can provide name of a pokemon and will get his image and basic information'
        ]
    
        return Response({'message': 'Pokemon', 'pokemon_species': pokemon_test_view})
    
class PokemonSpeciesViewSet(viewsets.ViewSet):
    """Test getting pokemon species by its name"""
    
    serializer_class = serializers.PokemonSerializer
    
    def list(self, request):
        """Return a Hello message"""
        pokemon_viewset = [
            'Users actions: list, create, retrieve, update, partial_update',
            'Automatically maps to URLs using ROuters',
            'Provides more functionality with less code'
        ]
        
        return Response({'message':'Hello', 'a_viewset': pokemon_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            pokemon_name = serializer.validated_data.get('pokemon_name')
            message = f'Hello {pokemon_name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating of an object"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})