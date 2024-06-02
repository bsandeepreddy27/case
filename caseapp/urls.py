from django.urls import path
from . import views

urlpatterns = [
    path('', views.homecase, name='homecase'),
    
    path('homecase', views.homecase, name='homecase'),

]
