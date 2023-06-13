from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bank_system import views


router = DefaultRouter()
router.register('account', views.AccountViewSet)

urlpatterns = [
    path('', views.to_login_view),
    path('index/', views.login_view),
    path('api', include(router.urls))
]