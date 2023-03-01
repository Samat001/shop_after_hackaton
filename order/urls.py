
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from order.views import OrderModelViewSet

router = DefaultRouter()
router.register('', OrderModelViewSet)

urlpatterns = [

    path('', include(router.urls))

]