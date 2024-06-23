from rest_framework.decorators import api_view, permission_classes
from ..serializers.recipes_serializers import RecipeSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from ..models import Recipe, Image
import json

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # Exige autenticação para acessar esta view
def create_recipe(request):
 
  if request.method == 'POST':
      data = request.data
      user = request.user

      # Salvando a imagem
      image = None
      if 'image' in request.FILES:
          image_file = request.FILES['image']
          image = Image.objects.create(name=image_file.name, image=image_file)

      recipe = Recipe.objects.create(
          title=data['title'],
          description=data['description'],
          created_by=user,
          ingredients=data['ingredients'],
          preparation_method=data['preparationMethod'],
          image=image
      )

      # Criando um dicionário com os dados da receita
      recipe_data = {
          'title': recipe.title,
          'description': recipe.description,
          'created_by': recipe.created_by.username,
          'ingredients': recipe.ingredients,
          'preparation_method': recipe.preparation_method,
          'created_at': recipe.created_at,
          'updated_at': recipe.updated_at,
          'image': request.build_absolute_uri(recipe.image.image.url) if recipe.image else None
      }
      return JsonResponse({'message': 'Receita criada com sucesso!', 'recipe': recipe_data})
  else:
      return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_all_recipes(request):
    recipes = Recipe.objects.all()
    recipe_data = []
    
    for recipe in recipes:
        recipe_dict = {
            'id': recipe.id,
            'title': recipe.title,
            'description': recipe.description,
            'ingredients': recipe.ingredients,
            'preparation_method': recipe.preparation_method,
            'created_by': recipe.created_by.username,
            'created_at': recipe.created_at,
            'updated_at': recipe.updated_at,
            'image_url': request.build_absolute_uri(recipe.image.image.url) if recipe.image else None
        }
        recipe_data.append(recipe_dict)
    
    return JsonResponse({'recipes': recipe_data})

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_recipe_by_id(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404('Receita não encontrada')
    
    recipe_data = {
        'id': recipe.id,
        'title': recipe.title,
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'preparation_method': recipe.preparation_method,
        'created_by': recipe.created_by.username,
        'created_at': recipe.created_at,
        'updated_at': recipe.updated_at,
        'image_url': request.build_absolute_uri(recipe.image.image.url) if recipe.image else None
    }

    return JsonResponse({'recipe': recipe_data})

@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated]) 
def update_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404('Receita não encontrada')

    if request.method == 'PUT':
        data = request.data

        # Atualiza os campos da receita com os novos dados
        recipe.title = data.get('title', recipe.title)
        recipe.description = data.get('description', recipe.description)
        recipe.ingredients = data.get('ingredients', recipe.ingredients)
        recipe.preparation_method = data.get('preparation_method', recipe.preparation_method)

        # Salva a imagem, se fornecida
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            image = Image.objects.create(name=image_file.name, image=image_file)
            recipe.image = image

        recipe.save()

        # Serializa a receita atualizada
        serializer = RecipeSerializer(recipe, context={'request': request})
        return JsonResponse({'message': 'Receita atualizada com sucesso!', 'recipe': serializer.data})

    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

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