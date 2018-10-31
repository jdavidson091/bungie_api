from django.db import models


class Weapon(models.Model):
    app_label = 'Weapon'

    weapon_name = models.CharField(max_length=50)
    rarity = models.CharField(max_length=50)
    impact = models.IntegerField(null=True)
    range = models.IntegerField(null=True)
    stability = models.IntegerField(null=True)
    magazine = models.IntegerField(null=True)
    reload_speed = models.IntegerField(null=True)
    handling = models.IntegerField(null=True)
    zoom = models.IntegerField(null=True)
    inventory_size = models.IntegerField(null=True)
    aim_assistance = models.IntegerField(null=True)
    recoil_direction = models.IntegerField(null=True)

    def __str__(self):
        return self.weapon_name
