from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('weapon/', views.weapon_list, name='all weapons'),
    path('weapon/<int:weapon_id>', views.weapon_list, name='specific weapon')
]
