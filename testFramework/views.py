from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User


# Create your views here.
class Test(APIView):
    def get(self, request):
        self.as_view()
        data = []
        user = User.objects.all()
        for i in user:
            data.append({'name': i.name, 'age': i.age, 'sex': i.sex, 'email': i.email})
        return Response(data)

    def post(self, request):
        self.as_view()
        email = request.data['email']
        name = request.data['name']
        age = request.data['age']
        sex = request.data['sex']
        data = {}
        print(name, age, sex, email)

        try:
            with transaction.atomic():
                create = User.objects.create(name=name, email=email, age=age, sex= sex)
                data['name'] = create.name
                data['email'] = create.email
                data['age'] = create.age
                data['sex'] = create.sex
                print(data)
        except Exception as e:
            data['Error'] = e

        return Response(data)
