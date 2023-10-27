from django.urls import path
from .views import CarsAPIList, CarsAPIUpdate, CarsAPIDestroy, PaymentView

urlpatterns = [
    path('content/', CarsAPIList.as_view()),
    path('content_u/<int:pk>', CarsAPIUpdate.as_view()),
    path('content_d/<int:pk>', CarsAPIDestroy.as_view()),
    path('payment/', PaymentView.as_view(), name='payment-list'),
]
