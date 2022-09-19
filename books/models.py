
from ast import mod
from django.db import models
from django.urls import reverse
from datetime import datetime



class Category1(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category2(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category3(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    category1 = models.ForeignKey(Category1, on_delete=models.CASCADE, default=1)
    category2 = models.ForeignKey(Category2, on_delete=models.CASCADE,blank=True,null=True, default=1)
    category3 = models.ForeignKey(Category3, on_delete=models.CASCADE,blank=True,null=True, default=1)
    title  = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    description = models.TextField(default=None)
    # price = models.FloatField(null=True, blank=True)
    images = models.ImageField(upload_to="shop/images", blank=True ,default="")
    image_url = models.CharField(max_length = 2083, blank=True)
    pdf=models.FileField(upload_to="pdf/", default="", blank=True ,null=True)
    pdfurl=models.CharField(max_length = 3000, blank=True)
    # follow_author = models.CharField(max_length=2083, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    seoclicks=models.IntegerField(default=0)
    book_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Book.objects.filter(category1 = category_id )
        else:
            return Book.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid2(category_id2):
        if category_id2:
            return Book.objects.filter(category2 = category_id2 )
        else:
            return Book.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid3(category_id3):
        if category_id3:
            return Book.objects.filter(category3 = category_id3 )
        else:
            return Book.objects.all()




class Review(models.Model):
    title = models.IntegerField()
    comment = models.TextField(default=None)
    user = models.CharField(max_length=40,default='Anonymous', blank=True)
    created = models.CharField(max_length=40)
    rating=models.IntegerField()
    def __str__(self):
        return self.created

    
