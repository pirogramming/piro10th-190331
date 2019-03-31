from django.urls import path

from bulletin import views

appname= "bulletin"

urlpatterns = [
    path('', views.documentList, name='board'),
    path('post/', views.newPost, name="new_post"),
    path('<int:id>/', views.detailView, name='document'),
    path('<int:id>/delete/', views.deleteDoc, name='delete_document'),
    path('<int:id>/modify/', views.modifyDoc, name='modify_document')

]