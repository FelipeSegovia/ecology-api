from rest_framework.response import Response
from rest_framework.decorators import api_view

from ecology.models import Ecology
from ecology.serializer import EcologySerializer

"""
class EcologyAPIView(APIView):

    def get(self, request):
        ecologies = Ecology.objects.all()
        ecology_serializer = EcologySerializer(ecologies, many=True)

        return Response(ecology_serializer.data)


"""


@api_view(['GET', 'POST'])
def ecology_api_view(request):
    if request.method == 'GET':
        ecologies = Ecology.objects.all()
        ecology_serializer = EcologySerializer(ecologies, many=True)

        return Response(ecology_serializer.data)

    elif request.method == 'POST':
        ecology_serializer = EcologySerializer(data=request.data)
        if ecology_serializer.is_valid():
            ecology_serializer.save()
            return Response(ecology_serializer.data)
        return Response(ecology_serializer.errors)
