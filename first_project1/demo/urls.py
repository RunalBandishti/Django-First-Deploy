from django.urls import path
from demo import views

urlpatterns = [
    path('',views.index,name='index'),
]