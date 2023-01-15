from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
from users.views import LoginView, UserViewSet


router = DefaultRouter()
router.register('users', UserViewSet, basename='user')


urlpatterns = [
    path('v1/login/', LoginView.as_view()),
    path('v1/logout/', knox_views.LogoutView.as_view()),
    path('v1/logoutall/', knox_views.LogoutAllView.as_view()),
    path('v1/', include(router.urls))
]
