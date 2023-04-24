from django.contrib import admin
from .models import *
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=['author_name','author_address']
admin.site.register(Author,AuthorAdmin)

class PublisherAdmin(admin.ModelAdmin):
    list_display=['publisher_name','publisher_address','phone']
admin.site.register(Publisher,PublisherAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=['customer_name','email','address','phone']
admin.site.register(Customer,CustomerAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=['book_author','book_publisher','title','price','release_date']
admin.site.register(Book,BookAdmin)
