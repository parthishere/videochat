from .views import home_view
from django.urls import path

app_name = 'main_app'

urlpatterns = [
    path('', home_view, name="home"),
]