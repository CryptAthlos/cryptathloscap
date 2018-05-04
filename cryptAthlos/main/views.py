from rest_framework.response import Response
from .models import Main
from .serializers import MainSerializer
from rest_framework.decorators import api_view


@api_view(['GET', ])
def get_main(request):
    # get all main
    cryptos = Main.objects.all()
    serializer = MainSerializer(cryptos, many=True)
    return Response(serializer.data)
