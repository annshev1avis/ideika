from django.urls import path, register_converter, include, re_path
from . import views
from . import converters


urlpatterns = [
    path('categories/', views.CategoriesView.as_view()),
    path('categories/<int:pk>/', views.CategoryView.as_view()),
    path('cards/', views.CardsListCreateView.as_view()),
    path('cards_by_cat/<int:category_id>/', views.CardsByCategoryListView.as_view()),
    path('cards_by_creator/<int:creator_id>/', views.CardsByCreatorListView.as_view()),
    path('cards/<int:pk>/', views.SingleCardView.as_view()),
    path('users/<int:user_id>/cards/', views.UserCollection.as_view()),
    path('users/<int:user_id>/cards/<int:card_id>/', views.UserCollection.as_view()),
    path('tags/', views.TegsListView.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
