from django.db import models


class Weapon(models.Model):
    weapon_name = models.CharField(max_length=50)
    rarity = models.CharField(max_length=50)
    impact = models.IntegerField()
    range = models.IntegerField()
    stability = models.IntegerField()
    magazine = models.IntegerField()
    reload_speed = models.IntegerField()
    handling = models.IntegerField()
    zoom = models.IntegerField()
    inventory_size = models.IntegerField()
    aim_assistance = models.IntegerField()
    recoil_direction = models.IntegerField()

    def __str__(self):
        return self.weapon_name
