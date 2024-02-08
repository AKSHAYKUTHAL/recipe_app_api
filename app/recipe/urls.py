# flake8: noqa
"""
URL mappings for the recipe app.
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]



# # urls.py
# from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from recipe import views

# # Define the URL patterns directly, mapping them to the appropriate viewset actions
# urlpatterns = [
#     # Recipe URLs
#     path('recipes/', views.RecipeViewSet.as_view({
#         'get': 'list',
#         'post': 'create'
#     }), name='recipe-list'),
#     path('recipes/<int:pk>/', views.RecipeViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     }), name='recipe-detail'),

#     # Tag URLs
#     path('tags/', views.TagViewSet.as_view({
#         'get': 'list',
#         'post': 'create'  # Assuming you want to add support for creating tags directly
#     }), name='tag-list'),
#     path('tags/<int:pk>/', views.TagViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     }), name='tag-detail'),

#     # Include more paths as needed
# ]

# # Optional: Use format_suffix_patterns to allow specifying format with URLs
# urlpatterns = format_suffix_patterns(urlpatterns)
