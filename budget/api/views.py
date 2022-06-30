from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from butce.models import Transaction
from .serializers import ItemSerializers


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/all',
        'Add': '/add',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['GET'])
def getData(request):
    items = Transaction.objects.all()
    serializer = ItemSerializers(items, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateItem(request, pk):
    item = Transaction.objects.get(id=pk)
    data = ItemSerializers(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteItem(request,pk):
    item = get_object_or_404(Transaction, id=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)