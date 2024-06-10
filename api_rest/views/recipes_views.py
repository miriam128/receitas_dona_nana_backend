from rest_framework.decorators import api_view, permission_classes
from ..serializers.recipes_serializers import RecipeSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from ..models import Recipe
import json

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # Exige autenticação para acessar esta view
def create_recipe(request):
 
  data = json.loads(request.body)
  user = request.user
  recipe = Recipe.objects.create(
    title=data['title'],
    description=data['description'],
    created_by=user,
    ingredients=data['ingredients'],
    preparation_method=data['preparationMethod']
  )

  # Criando um dicionário com os dados da receita
  recipe_data = {
    'title': recipe.title,
    'description': recipe.description,
    'created_by': recipe.created_by.username,
    'ingredients': recipe.ingredients,
    'preparation_method': recipe.preparation_method,
    'created_at': recipe.created_at,
    'updated_at': recipe.updated_at
  }
  return JsonResponse({'message': 'Receita criada com sucesso!', 'recipe': recipe_data})

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # Exige autenticação para acessar esta view
def list_all_recipes(request):
  recipes = Recipe.objects.all()
  serializer = RecipeSerializer(recipes, many=True)
  return JsonResponse({'recipes': serializer.data})

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # Exige autenticação para acessar esta view
def get_recipe_by_id(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404('Receita não encontrada')
    
    serializer = RecipeSerializer(recipe)
    return JsonResponse({'recipe': serializer.data})

@csrf_exempt
@api_view(['DELETE'])  # Defina o método HTTP como DELETE para a view de exclusão
@permission_classes([IsAuthenticated])
def delete_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404('Receita não encontrada')

    recipe.delete()
    return JsonResponse({'message': 'Receita excluída com sucesso!'})