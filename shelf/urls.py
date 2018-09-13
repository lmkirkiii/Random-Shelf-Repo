from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ultra_treasure_list, name='ultra_treasure_list'),
    path('ultra_treasures/list', views.ultra_treasure_list, name='ultra_treasure_list'),
    path('ultra_treasures/<int:pk>', views.ultra_treasure_detail, name='ultra_treasure_detail'),
    path('ultra_treasures/new', views.ultra_treasure_create, name='ultra_treasure_create'),
    path('ultra_treasures/<int:pk>/edit', views.ultra_treasure_edit, name='ultra_treasure_edit'),
    path('ultra_treasures/<int:pk>/delete', views.ultra_treasure_delete, name='ultra_treasure_delete'),
    path('accounts/signup/', views.sign_up, name='signup'),
    
]
