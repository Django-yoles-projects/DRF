from django.urls import path
from .views import basic_serialize

app_name = "base"

urlpatterns = [
    path('serialize', basic_serialize, name='serialize')    
]