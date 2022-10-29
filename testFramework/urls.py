from django.urls import path
from .views import PaymentApi, home

urlpatterns = [
    path('', home),
    path('api/Cost/', PaymentApi.as_view())
]