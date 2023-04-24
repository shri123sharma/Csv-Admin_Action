from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Author(models.Model):
    author_name=models.CharField(max_length=255,null=False,blank=False)
    author_address=models.CharField(max_length=255,null=False,blank=False)

    def __str__(self):
        return self.author_name
    
class Publisher(models.Model):
    publisher_name=models.CharField(max_length=255,null=False,blank=False)
    publisher_address=models.CharField(max_length=255,null=False,blank=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.publisher_name
class Customer(models.Model):
    customer_name=models.CharField(max_length=255,null=False,blank=False)
    email=models.EmailField(max_length=255,null=False,blank=False,unique=True)
    address=models.CharField(max_length=255,null=False,blank=False)
    phone=PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.customer_name

class Book(models.Model):
    book_author=models.ForeignKey(Author,null=True,blank=True,related_name='author_book',on_delete=models.CASCADE)
    book_publisher=models.ForeignKey(Publisher,null=True,blank=True,related_name='publisher_book',on_delete=models.CASCADE)
    title=models.CharField(max_length=255,null=False,blank=False)
    price=models.PositiveIntegerField()
    release_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    

