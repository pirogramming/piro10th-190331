from django.urls import path

from bulletin import views

appname= "bulletin"

urlpatterns = [
    path('', views.documentList, name='board'),
    path('<int:id>/', views.detailView, name='document')
]