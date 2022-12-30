from django.urls import path
from . import views

urlpatterns = [
    path('Adjectives/', views.Adjectives.as_view(),
         name='Adjectives'),
    path('Categorize/', views.Categorize.as_view(),
         name='Categorize'),
    path('Nouns/', views.Nouns.as_view(),
         name='Nouns'),
    path('RankPositiveSentiments/', views.RankPositiveSentiments.as_view(),
         name='RankPositiveSentiments'),
    path('RankNegativeSentiments/', views.RankNegativeSentiments.as_view(),
         name='RankNegativeSentiments'),
]
