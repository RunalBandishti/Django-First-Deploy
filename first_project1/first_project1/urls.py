
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from demo import views
urlpatterns = [
    path('',views.index,name='index'),
    path('demo/',include('demo.urls')),
    path('admin/', admin.site.urls),
]
