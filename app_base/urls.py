from django.urls import path
from app_base.views import *

urlpatterns = [
    path('', home, name='home'),
]