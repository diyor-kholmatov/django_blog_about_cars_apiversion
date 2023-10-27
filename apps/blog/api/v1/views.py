from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import CarsSerializer, PaymentSerializer
from apps.blog.models import Cars, Payment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from cloudpayments import CloudPayments


class CarsAPIList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CarsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticated, )


class CarsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAdminUser, )


class PaymentView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()

            # Генерация токена в CloudPayments
            cloudpayments = CloudPayments()
            token = cloudpayments.generate_token(
                amount=payment.amount,
                currency='RUB',
                name=payment.description,
            )

            payment.token = token
            payment.save()

            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

