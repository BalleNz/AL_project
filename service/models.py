from django.db import models


class Element(models.Model):
    element_update_date = models.DateField
    action_start = models.DateField
    action_end = models.DateField
    action_name = models.CharField(max_length=200)
    action_place = models.CharField(max_length=100, blank=True)
    action_category = models.CharField(max_length=100)
    action_region = models.CharField(max_length=100)
    action_about = models.TextField(blank=True)
    action_organization = models.TextField
    action_coordinates = models.CharField(max_length=50)
    action_limit_age = models.SmallIntegerField
    action_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    action_max_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
