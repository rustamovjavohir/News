from django.urls import path
from accout.views import sign_in, register, sign_out

app_name = 'auth'
urlpatterns = [
    path('login/', sign_in, name='login'),
    path('register/', register, name='register'),
    path('logout/', sign_out, name='logout'),
]
