from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.contrib.auth import get_user_model
from order.models import Order 
from order.views import OrderModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
User = get_user_model()

class OrderTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.setUp_user()
        self.setup_user_token()
        self.access_token = self.setup_user_token()
        # self.test_get_order()
    
    def setUp_user(self):
        self.user = User.objects.create_user(
            email = 'test@test.com',
            password = '1',
            is_active = True    
        )    


    def setup_user_token(self):
        # print(self.user, '!!!!!!!!')
        data = {
            "email": "test@test.com",
            "password": "1"
        }
        request = self.factory.post('api/v1/account/login/' , data)
        view = TokenObtainPairView.as_view()
        # print(request, '!!!!!!!!!!!')
        response = view(request)
        # print(response.data, '!!!!!!')
        return response.data['access']
        


    def test_get_order(self):
        request = self.factory.get('api/v1/order/', HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        view = OrderModelViewSet.as_view({'get':'list'})
        # force_authenticate(request, self.user)
        
        response = view(request)
        assert response.status_code == 200


#     owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
#     status = models.CharField(max_length=30,choices=ORDER_STATUS,null=True,blank=True)
#     is_confirm = models.BooleanField(default=False)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='orders')
#     addres = models.TextField()
#     number = models.CharField(max_length=30)
#     total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
#     amount = models.PositiveIntegerField()
#     created_add = models.DateTimeField(auto_now_add=True)
#     activation_code = models.UUIDField(default=uuid.uuid4)



