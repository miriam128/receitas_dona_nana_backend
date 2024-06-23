"""
URL configuration for api_root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from api_rest.views.recipes_views import create_recipe, list_all_recipes, get_recipe_by_id, delete_recipe, update_recipe
from api_rest.views.users_views import register_user, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Recipe
    path('recipe/create/', create_recipe, name='create_recipe'),
    path('recipe/<int:recipe_id>/show/', get_recipe_by_id, name='get_recipe_by_id'),
    path('recipe/index/', list_all_recipes, name='list_all_recipes'),
    path('recipe/<int:recipe_id>/edit/', update_recipe, name='update_recipe'),
    path('recipe/<int:recipe_id>/delete/', delete_recipe, name='delete_recipe'),

    # User
    path('register/', register_user, name='register_user'),
    path('login/', login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
