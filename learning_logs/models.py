from django.db import models

# Create your models here.
# Page 503
class Topic(models.Model):
    """Topic displayed for users"""
    text = models.CharField(max_length=200) #pole text czyli nazwa tematu, Charfield określa max długość znaków
    date_added = models.DateTimeField(auto_now_add=True) #pole data określone po aktualnej dacie i godzinie dodania

    def __str__(self):
        """Zwraca textową reprezentację modelu"""
        return self.text