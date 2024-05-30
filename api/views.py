from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializer import ItemSerializer

# Create your views here.


@api_view(['GET'])
def Getdata(request):
    item = Item.objects.all()
    serializer = ItemSerializer(item, )
    return Response ()
