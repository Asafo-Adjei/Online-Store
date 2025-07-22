from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)   #This is to order the categories in aplhabetical order
        verbose_name_plural = 'Categories'  #This code is written to correct the wrong plural spelling in the admin panel

    def __str__(self):  #The underscores are double on both sides of the word "str"
        return self.name  #This line of code is to return the actual names of the created categories in the admin instead of the default names given by the system
    

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)  #"on_delete=models.CASCADE" ensures that if a category is deleted all of its items are deleted as well
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  #blank and null are = "True" incase a user does not want to provide one
    price = models.FloatField() 
    image = models.ImageField(upload_to='item_images', blank=True, null=True) #item_images is a folder that the images are uploaded to
    is_sold = models.BooleanField(default=False)
    created_by =models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)  #"on_delete=models.CASCADE" ensures that if a user is deleted all of his items are deleted as well
    created_at = models.DateTimeField(auto_now_add=True) #date for when item was added/created

    def __str__(self):
        return self.name
