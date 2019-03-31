from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('signup',signup, name='signup'),
    path('signin', signin, name='signin'),
]