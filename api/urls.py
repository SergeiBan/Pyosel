from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
from users.views import LoginView, RegisterViewSet, UserViewSet
from animals.views import AnimalViewSet, LostProfileViewSet, FoundProfileViewSet


router = DefaultRouter()
router.register('register', RegisterViewSet, basename='register')
router.register('users', UserViewSet, basename='user')
router.register('animals', AnimalViewSet, basename='animal')
# router.register('found', FoundViewSet, basename='found')
router.register('lost_profiles', LostProfileViewSet, basename='lost_profile')
router.register('found_profiles', FoundProfileViewSet, basename='found_profile')


urlpatterns = [
    path('v1/login/', LoginView.as_view()),
    path('v1/logout/', knox_views.LogoutView.as_view()),
    path('v1/logoutall/', knox_views.LogoutAllView.as_view()),
    path('v1/', include(router.urls))
]
