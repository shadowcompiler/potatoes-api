from django.urls import path, include
from potatoes import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, basename='hello-viewset')
router.register('profile', views.UserProfileViewset,)
router.register('feed', views.UserFeedViewset,)

urlpatterns = [
    path('hello-view/', views.HelloWorld.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
