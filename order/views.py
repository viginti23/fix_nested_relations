from rest_framework import status, authentication, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer, MyOrderSerializer


class CheckoutView(GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        paid_amount = sum(item.get('total_price') for item in serializer.validated_data['items'])
        data = {
            'paid_amount': paid_amount,
            'user': request.user
        }
        return Response(data=data.update(serializer.data), status=status.HTTP_201_CREATED)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
