
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('applications.home.urls')),
    path('admin/', admin.site.urls),
]
