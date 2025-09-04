from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework.response import Response

from .filters import MuseumFilter
from .models import Museum
from .serializers import MuseumAdminAccessSerializer, MuseumSerializer

# from rest_framework.views import APIView
# from rest_framework.viewsets import ViewSet


# Create your views here.


    
class MuseumListAPIView(generics.ListCreateAPIView):

    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer
    filterset_class = MuseumFilter
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
    def post(self, request):
    # Deserialize the incoming data
        serializer = MuseumSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():

            # Save the new post
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            
            # return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class MuseumAdminViewSet(viewsets.ModelViewSet):


    queryset = Museum.objects.all()
    serializer_class = MuseumAdminAccessSerializer 
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

    
    def museum_detail(request, pk):
        try:
            museum = Museum.objects.get(pk=pk)
        except Museum.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = MuseumSerializer(museum)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = MuseumSerializer(museum, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            museum.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
    # def get_permissions(self):
    #     self.permission_classes = [AllowAny]
    #     if self.request.method == 'POST':
    #         self.permission_classes = [IsAdminUser]
    #     return super().get_permissions()
