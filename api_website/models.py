from django.db import models
from django.utils import timezone
import requests
from django.urls import reverse
from django.contrib.auth.models import User

cocktail_url = 'https://www.thecocktaildb.com/api/json/v1/1/'
# random_param = "random.php"
# ingredient_param = "filter.php?i="
# id_param = "lookup.php?i="
letter_param = "search.php?f=d"

response = requests.get(url=cocktail_url + letter_param)
data = response.json()["drinks"]


# Create your models here.

#
class Chrab(models.Model):
    drink_name = models.CharField(max_length=400)
    glass = models.CharField(max_length=400)
    first_ingredient = models.CharField(max_length=400, null=True)
    second_ingredient = models.CharField(max_length=400, null=True)
    third_ingredient = models.CharField(max_length=400, null=True)
    fourth_ingredient = models.CharField(max_length=400, null=True)
    instructions = models.CharField(max_length=1000)
    drink_image = models.CharField(max_length=400)
    first_ingredient_measurements = models.CharField(max_length=400, null=True)
    second_ingredient_measurements = models.CharField(max_length=400, null=True)
    third_ingredient_measurements = models.CharField(max_length=400, null=True)
    fourth_ingredient_measurements = models.CharField(max_length=400, null=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.drink_name

    def get_absolute_url(self):
        return reverse('api_website-cocktails')

    #     # return self.glass
    #     # return self.first_ingredient
    # return self.second_ingredient
    # return self.third_ingredient
    # return self.fourth_ingredient
    # return self.instructions
    # return self.drink_image
    # return self.first_ingredient_measurements
    # return self.second_ingredient_measurements
    # return self.third_ingredient_measurements
    # return self.fourth_ingredient_measurements


def post_db(data):
    for drink in data:
        new_drink = Chrab(drink_name=drink['strDrink'], glass=drink['strGlass'],
                          first_ingredient=drink["strIngredient1"], second_ingredient=drink["strIngredient2"],
                          third_ingredient=drink["strIngredient3"], fourth_ingredient=drink["strIngredient4"],
                          instructions=drink["strInstructions"], drink_image=drink["strDrinkThumb"],
                          first_ingredient_measurements=drink["strMeasure1"],
                          second_ingredient_measurements=drink["strMeasure2"],
                          third_ingredient_measurements=drink["strMeasure3"],
                          fourth_ingredient_measurements=drink["strMeasure4"])

        new_drink.save()

# post_db(data=data)
