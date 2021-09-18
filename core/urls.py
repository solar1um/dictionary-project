from django.contrib import admin
from django.urls import path
from dictionary.views import dict

urlpatterns = [
    path('admin/', admin.site.urls),
    path('words/', dict)
]
