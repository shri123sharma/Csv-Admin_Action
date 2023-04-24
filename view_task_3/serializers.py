from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class PublisherSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields='__all__'

class CustomerSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
    
class BookSerilaizer(serializers.ModelSerializer):
    book_author=serializers.SerializerMethodField()
    book_publisher=serializers.SerializerMethodField()
    class Meta:
        model=Book
        fields=['book_author','book_publisher','title','price','release_date']

    def get_book_author(self,obj):
        book_author=Author.objects.filter(author_book__id=obj.id)
        if book_author:
          return AuthorSerializer(book_author,many=True).data
        else:
            ''
    def get_book_publisher(self,obj):
        book_publisher=Publisher.objects.filter(publisher_book__id=obj.id)
        if book_publisher:
            return PublisherSerilaizer(book_publisher,many=True).data
        else:
            ''
            