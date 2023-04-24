from django.urls import path
from django import views
from .views import *

urlpatterns = [
    
    path('author/',AuthorListView.as_view(),name='author_list'),
    path('author/<int:pk>/',AuthorDetailView.as_view(),name='author_detail'),
    path('publisher_list/',PublisherListView.as_view(),name='publisher_list'),
    path('publisher_create/',PublisherCreateView.as_view(),name='publisher_create'),
    path('customer_list_create/',CustomerListCreateView.as_view(),name='customer_list_create'),
    path('book_list_create/',BookListCreateView.as_view(),name='book_list_create'),
    path('book_retrive_update_delete/<int:pk>/',BookRetriveUpdateDeleteView.as_view(),name='book_retrive_update_delete'),
    path('book_list/',BookListView.as_view(),name='book_list'),
    
]

