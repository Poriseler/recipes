from django.urls import path
from rest_framework import routers
from .views import RecipeViewSet

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet, 'recipes')

urlpatterns = router.urls
#urlpatterns =[

#]