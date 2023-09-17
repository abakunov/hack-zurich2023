from django.urls import path, include
from rest_framework.generics import CreateAPIView
from .views import *

api_urls = [
    path('get-map/', GetAllUsersView.as_view()),
    path('update-user/', CreateOrUpdateUserView.as_view()),
    path('update-location/', UpdateLocationView.as_view()),
    path('all-tags/', GetTagsView.as_view()),
    path('get-avatars/', GetAvatarsView.as_view()),
]