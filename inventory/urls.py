from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodItemViewSet

router = DefaultRouter()
router.register(r'foods', FoodItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
