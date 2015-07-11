from django.contrib.auth import authenticate

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import detail_route

from .serializers import UserSerializer, UserLocationSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        return Response([])

    def update(self, request, pk=None, **kwargs):
        return super(UserViewSet, self).update(request, pk, partial=True)


class ObtainAuthToken(APIView):

    def post(self, request):
        user = authenticate(username=request.DATA['username'], password=request.DATA['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UserSerializer(user).data})
        return Response('Invalid username or password', status=status.HTTP_400_BAD_REQUEST)
