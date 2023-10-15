from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import CarsSerializer
from apps.blog.models import Cars


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
