from django.urls import path
from . import views

urlpatterns = [
    path('',views.App,name='app'),
    # path('about/',views.about,name='about'),
   
]
