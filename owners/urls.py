from django.urls import path
from owners.views import OwnerListView, DogListView

urlpatterns = [
    path('/owners', OwnerListView.as_view()),
    path('/dogs', DogListView.as_view())
]
