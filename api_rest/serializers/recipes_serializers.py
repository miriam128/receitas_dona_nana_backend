from rest_framework import serializers
from ..models import Recipe
from .images_serializers import ImageSerializer

class RecipeSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, recipe):
        if recipe.image:
            return self.context['request'].build_absolute_uri(recipe.image.url)
        return None

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'ingredients', 'preparation_method', 'created_by', 'created_at', 'updated_at', 'image_url')