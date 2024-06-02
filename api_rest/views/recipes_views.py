from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    'created_by': recipe.created_by.username,  # ou qualquer outro campo relevante do usuário
    'ingredients': recipe.ingredients,
    'preparation_method': recipe.preparation_method,
    'created_at': recipe.created_at,
    'updated_at': recipe.updated_at
  }
  return JsonResponse({'message': 'Receita criada com sucesso!', 'recipe': recipe_data})
