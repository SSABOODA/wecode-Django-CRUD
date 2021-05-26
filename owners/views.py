import json

from django.db.models.fields.related import ForeignKey
from django.http import JsonResponse
from django.views import View
from .models import Owner, Dog


class OwnerListView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data['name'],
                             email=data['email'],
                             age=data['age'])

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):

        owners = Owner.objects.all()
        result = []
        for owner in owners:
            value = owner.dog_set.all()
            dog_result = []

            for dog in value:
                dog_result.append(
                    {
                        'name': dog.name,
                        'age': dog.age
                    }
                )
            result.append(
                {
                    'name': owner.name,
                    'age': owner.age,
                    'email': owner.email,
                    'my dog': dog_result
                }
            )

        return JsonResponse({'result': result}, status=200)

        #####################################################################################################################################################################################################################################################


class DogListView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(name=data['name'],
                           age=data['age'],
                           owner=Owner.objects.get(name=data['owner'])
                           )

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()

        result = []
        for dog in dogs:
            result.append(
                {
                    'name': dog.name,
                    'age': dog.age,
                    'master': dog.owner.name
                }
            )

        return JsonResponse({'MESSAGE': result}, status=200)
