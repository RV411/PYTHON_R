from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name=models.models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

class Post(models.Model):

    category=models.models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

