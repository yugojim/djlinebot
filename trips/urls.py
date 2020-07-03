from django.conf.urls import include, url
from django.urls import path
from mysite import views

app_name = 'trips'

urlpatterns = [
    path('', views.index),
#    path('books/', views.BookListView.as_view(), name='books'),
]