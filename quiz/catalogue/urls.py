from django.urls import path
from . import views
from .views import index
app_name = 'catalogue'


urlpatterns= [
   path('', index, name='index'),
   
    
]
    
