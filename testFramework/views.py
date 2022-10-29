from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Payment


# Create your views here.
def home(request):
    return render(request, 'index.html')
class PaymentApi(APIView):
    def get(self, request):
        self.as_view()
        data = []
        payment = Payment.objects.all()
        for result in payment:
            data.append({'name': result.user.name, 'cost': result.cost})
        return Response(data)


# class Test(APIView):
#     def get(self, request):
#         self.as_view()
#         data = []
#         user = User.objects.all()
#         for i in user:
#             data.append({'name': i.name, 'age': i.age, 'sex': i.sex, 'email': i.email})
#         return Response(data)
#
#     def post(self, request):
#         self.as_view()
#         email = request.data['email']
#         name = request.data['name']
#         age = request.data['age']
#         sex = request.data['sex']
#         data = {}
#         print(name, age, sex, email)
#
#         try:
#             with transaction.atomic():
#                 create = User.objects.create(name=name, email=email, age=age, sex= sex)
#                 data['name'] = create.name
#                 data['email'] = create.email
#                 data['age'] = create.age
#                 data['sex'] = create.sex
#                 print(data)
#         except Exception as e:
#             data['Error'] = e
#
#         return Response(data)

