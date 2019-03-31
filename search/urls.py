from django.urls import path
from search import views

app_name = 'search'

urlpatterns = [
    path('', views.test, name='test'),
    path('result/', views.search, name='search')
]