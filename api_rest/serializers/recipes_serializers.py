from rest_framework import serializers
from ..models import Recipe
from .images_serializers import ImageSerializer

class RecipeSerializer(serializers.ModelSerializer):
    
    image = ImageSerializer()
    
    class Meta:
        model = Recipe
        fields = '__all__'