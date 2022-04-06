from django.urls import path, include

from rest_framework.routers import DefaultRouter

from pokemon_api import views

router = DefaultRouter()
router.register('pokemon', views.PokemonSpeciesViewSet, base_name='pokemon-viewset')

urlpatterns = [
    path('pokemon-view/', views.PokemonSpeciesView.as_view()),
    path('', include(router.urls)),
]
