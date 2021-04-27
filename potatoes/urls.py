from django.urls import path, include
from potatoes import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloWorld.as_view()),
    path('', include(router.urls)),
]
