from rest_framework import serializers
from destinyapp.bungie.models import Weapon


class WeaponSerializer(serializers.Serializer):
    weapon_name = serializers.CharField(max_length=50)
    rarity = serializers.CharField(required=True, allow_blank=False, max_length=50)
    impact = serializers.IntegerField()
    range = serializers.IntegerField()
    stability = serializers.IntegerField()
    magazine = serializers.IntegerField()
    reload_speed = serializers.IntegerField()
    handling = serializers.IntegerField()
    zoom = serializers.IntegerField()
    inventory_size = serializers.IntegerField()
    aim_assistance = serializers.IntegerField()
    recoil_direction = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Weapon` instance, given the validated data.
        """
        return Weapon.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Weapon` instance, given the validated data.
        """
        instance.weapon_name = validated_data.get('title', instance.title)
        instance.rarity = validated_data.get('title', instance.title)
        instance.impact = validated_data.get('title', instance.title)
        instance.range = validated_data.get('title', instance.title)
        instance.stability = validated_data.get('title', instance.title)
        instance.magazine = validated_data.get('title', instance.title)
        instance.reload_speed = validated_data.get('title', instance.title)
        instance.handling = validated_data.get('title', instance.title)
        instance.zoom = validated_data.get('title', instance.title)
        instance.inventory_size = validated_data.get('title', instance.title)
        instance.aim_assistance = validated_data.get('title', instance.title)
        instance.recoil_direction = validated_data.get('title', instance.title)
        instance.save()
        return instance
