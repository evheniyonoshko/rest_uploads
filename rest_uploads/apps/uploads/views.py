import random, string

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from uploads.permissions import IsOwnerOrReadOnly
from uploads.models import Upload
from uploads.serializers import UserSerializer, AuthUploadsSerializer


def detail(request, file_id):
    image = get_object_or_404(Upload, pk=file_id)
    return render(request, 'detail.html', {'image': image})


class Logout(APIView):
    queryset = User.objects.all()

    def delete(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UploadsList(generics.ListCreateAPIView):
    lookup_field = 'key'
    serializer_class = AuthUploadsSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        try:
            Upload.objects.get(key=key)
            self.perform_create(serializer)
        except:
            serializer.save(owner=self.request.user, key=key)
        serializer.save(owner=self.request.user, )

    def get_queryset(self):
        queryset = Upload.objects.filter(owner= self.request.user.id)
        return queryset



class UploadsDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field= 'key'
    def get_serializer_class(self):
        if self.request.user and self.request.user.is_authenticated():
            serializer_class = AuthUploadsSerializer
        return serializer_class

    queryset = Upload.objects.all()
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
