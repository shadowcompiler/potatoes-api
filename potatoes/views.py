from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (status, viewsets, filters)
from potatoes import (serializers, models, permissions,)
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

class HelloWorld(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditionnal Django View',
        'Gives you a most controol over you app logig',
        'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Update an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Partial update"""
        return Response({'methode':'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewset(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses actions(list, create, retrieve,  update, partial_update, destroy)',
            'utomatically maps to URLs using Routers'
        ]
        return Response({'message' : 'hello!', 'viewset':a_viewset})


    def create(self, request):
        """create method"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            return Response({'message': f'Ohayo {name}'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):

        return Response({'Http' : 'Delete'})

    def update(self, request, pk=None):

        return Response({'Http' : 'update'})

    def partial_update(self, request, pk=None):

        return Response({'Http' : 'partial_update'})


    def retrieve(self, request, pk=None):

        return Response({'Http' : 'get'})


class UserProfileViewset(viewsets.ModelViewSet):
    """Profile viewset"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserFeedViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserFeedSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = models.UserFeed.objects.all()
    permission_classes = (IsAuthenticated, permissions.UpdateOwnStatus)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
