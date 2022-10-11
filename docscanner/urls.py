from django.urls import path

from docscanner import views

urlpatterns = [
    path('', views.index, name='index'),
    path('texthand', views.texthand, name='texthand'),
    path('texthand/process/', views.processHandtoText, name='texthand'),
    
    
    
]