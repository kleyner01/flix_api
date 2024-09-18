from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorsCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', views.ActoRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
