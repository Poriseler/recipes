from django.db import models

# Create your models here.

class Recipe(models.Model):
    type_choice = [
        ('BR','Breakfast'),
        ('DN','Dinner'),
        ('SP','Supper'),
        ('DR','Drink'),
        ('VG','Vegan')
    ]

    ingredients_choice = [
        ('meat',(
            ('lamb','Lamb'),
            ('beef','Beef'),
            ('chicken','Chicken')
            )
         ),
        ('fish',(
            ('salmon','Salmon'),
            ('tuna','Tuna')
            )
         ),
        ('oil',(
            ('rapeseed','Rapeseed'),
            ('olive','Olive'),
            ('sunflower','sunflower')
            )
         )
    ]

    name = models.CharField(max_length=100)
    ingredients = models.CharField(choices=ingredients_choice, max_length=4, default='meat')
    type = models.CharField(max_length=2, choices=type_choice, default='BR')
    estimated_time = models.IntegerField(default=10)
    steps = models.TextField(default="Write some steps")