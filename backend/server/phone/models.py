from django.db import models

# Create your models here.

class Phone(models.Model):
    brand_name = models.CharField(max_length=50) # might be intergerfield with choices
    model_name = models.CharField(max_length=50)
    os = models.CharField(max_length=50) # might be integerfield with choices
    popularity = models.IntegerField()
    best_price = models.IntegerField()
    lowest_price = models.IntegerField()
    highest_price = models.IntegerField()
    sellers_amount = models.IntegerField()
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    memory_size = models.IntegerField()
    battery_size = models.IntegerField()
    release_date = models.DateField()
    image_url = models.URLField(max_length=200, null=True, blank=True)

