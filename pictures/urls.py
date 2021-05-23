from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='homepage'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
