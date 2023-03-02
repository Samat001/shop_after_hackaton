from rest_framework.routers import DefaultRouter
from django.urls import  path
from product.views import *

# router = DefaultRouter()
# router.register('', )

urlpatterns = [
    path('func_get/', get_product),
    path('func_post/',post_product),
    path('generic_get/', ProductListGenericView.as_view()),
    path('generic_post/', ProductCreateGenericView.as_view()),
    path('generic_get_post/',ProductListCreateGenericview.as_view()),
    path('api_get_post/', ProductAPIView.as_view()),
]