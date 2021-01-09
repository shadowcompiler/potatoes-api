from django.urls import path
from potatoes import views


urlpatterns = [
    path('hello-view/', views.HelloWorld.as_view()),
]
