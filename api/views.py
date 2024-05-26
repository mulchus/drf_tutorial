from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RequestView(APIView):
    queryset = Item.objects.all()

    @staticmethod
    def get(request):
        print(request.GET.dict())
        return Response(request.GET.dict(), status=status.HTTP_200_OK)
        # items = Item.objects.all()
        # serializer = ItemSerializer(items, many=True)
        # return Response(serializer.data)

    @staticmethod
    def post(request):
        print(request.POST.dict())
        return Response(request.POST.dict())
        # serializer = ItemSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
