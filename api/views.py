from django.db.models import query
from django.http import request
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from core.models import *


class CreateOrUpdateUserView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        # try:
            user, created = User.objects.get_or_create(uiid=request.data['uiid'])
            if request.data['nickname']:
                user.nickname = request.data['nickname']
            if request.data['bio']:
                user.bio = request.data['bio']
            if request.data['picture']:
                user.picture = request.data['picture']
            if request.data['lat']:
                user.lat = request.data['lat']
            if request.data['long']:
                user.long = request.data['long']
            if request.data['tags']:
                user.tags.clear()
                for tag in request.data['tags']:
                    user.tags.add(Tag.objects.get(id=tag))
            user.save()
            return Response(status=status.HTTP_200_OK)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
    

class GetAllUsersView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        users = User.objects.all()
        data = []
        for user in users:
            data.append({
                'uiid': user.uiid,
                'nickname': user.nickname,
                'bio': user.bio,
                'lat': user.lat,
                'long': user.long,
                'picture': user.picture.url if user.picture else None,
                'tags': [tag.name for tag in user.tags.all()]
            })
        return Response(data=data, status=status.HTTP_200_OK)


class UpdateLocationView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            user = User.objects.get(uiid=request.data['uiid'])
            user.lat = request.data['lat']
            user.long = request.data['long']
            user.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetTagsView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        tags = Tag.objects.all()
        data = []
        for tag in tags:
            data.append({
                'id': tag.id,
                'name': tag.name,
            })
        return Response(data=data, status=status.HTTP_200_OK)
