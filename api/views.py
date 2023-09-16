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
        try:
            user, created = User.objects.get_or_create(uuid=request.data['uuid'])
            if 'nickname' in request.data:
                user.nickname = request.data['nickname']
            if 'bio' in request.data:
                user.bio = request.data['bio']
            if 'picture' in request.data:
                user.picture = request.data['picture']
            if 'lat' in request.data:
                user.lat = request.data['lat']
            if 'long' in request.data:
                user.long = request.data['long']
            if 'tags' in request.data:
                user.tags.clear()
                for tag in request.data['tags'].split(','):
                    user.tags.add(Tag.objects.get(id=int(tag)))
            user.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class GetAllUsersView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        users = User.objects.all()
        data = []
        for user in users:
            data.append({
                'uuid': user.uuid,
                'nickname': user.nickname,
                'bio': user.bio,
                'lat': user.lat,
                'long': user.long,
                'picture': user.picture.url if user.picture else None,
                'tags': [{'id': tag.id, 'name': tag.name} for tag in user.tags.all()]
            })
        return Response(data=data, status=status.HTTP_200_OK)


class UpdateLocationView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            user = User.objects.get(uuid=request.data['uuid'])
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