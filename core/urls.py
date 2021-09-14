from django.contrib import admin
from django.urls import path
from dictionary.views import dictionary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('words/', dictionary)
]
