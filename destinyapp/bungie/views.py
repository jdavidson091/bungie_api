from destinyapp.bungie.models import Weapon
from destinyapp.bungie.serializers import WeaponSerializer
from rest_framework import generics


class WeaponList(generics.ListCreateAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class WeaponDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
