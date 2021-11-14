from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    line = models.TextField()
    color = models.TextField()
    transmition = models.TextField()
    model = models.TextField()
    category = models.ForeignKey(
        Category, related_name="cars", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
