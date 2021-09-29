from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('output/', views.output, name='output'),
    path('compare/', views.compare, name='compare'),
    path('test/', views.test, name='test'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)