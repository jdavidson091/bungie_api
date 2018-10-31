from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from destinyapp.bungie import views

urlpatterns = [
    path('weapon/', views.WeaponList.as_view()),
    path('weapon/<int:pk>/', views.WeaponDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
