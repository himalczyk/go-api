from rest_framework import serializers

from profiles_api import models

class PokemonSerializer(serializers.Serializer):
    """Serializers a name field for testing our Pokemon API view"""
    
    pokemon_name = serializers.CharField(max_length=36)