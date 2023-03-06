from rest_framework.routers import DefaultRouter
from django.urls import  path, include
from product.views import *

router = DefaultRouter()
router.register('view_set_get_post', ProductViewSet , basename='products' )
router.register('modelviewset_crud', ProductModelviewSet)
router.register('product_mixin', productMixin)

urlpatterns = [
    path('func_get/', get_product),
    path('func_post/',post_product),
    path('generic_get/', ProductListGenericView.as_view()),
    path('generic_post/', ProductCreateGenericView.as_view()),
    path('generic_get_post/',ProductListCreateGenericview.as_view()),
    path('api_get_post/', ProductAPIView.as_view()),
    # path('view_set_get_post/', ProductViewSet.as_view({'get':'list','post': 'create'})),
    path('hello/', get_hello),
    path('', include(router.urls)),
]