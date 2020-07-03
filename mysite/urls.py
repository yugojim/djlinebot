from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from trips.views import index,about,services,news,contact,linebot
from mysite import views

admin.site.site_header = 'User rights management'
app_name = 'mysite'

urlpatterns = [
    url(r'^$', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('news/', news, name='news'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
    path('base/', views.baseform),
    path('linebot/', linebot, name='linebot'),
    
    url(r'^trips/', views.index,name='trips'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('baseindex/', views.baseindex),
        # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]