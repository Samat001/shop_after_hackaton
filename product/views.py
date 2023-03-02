from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework import status , generics
from rest_framework.views import APIView


@api_view(['GET'])
def get_product(request):
    '''
    Get all product
    '''
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_product(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(owner=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductListGenericView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateGenericView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated ,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductListCreateGenericview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated ,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        return Response('GEEEEEEEEEEEEEEEEEEEEEEEEET')


    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#VIEWSET , MODELWUWSET , MIXINS

