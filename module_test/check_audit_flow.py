from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
import reversion
from reversion.models import Version
from module_test.serializers import *
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'items': data
        })


def creat_user():
    user = User.objects.create(
        username="kashida13",
        email="kk@gmail.com"
    )
    user.set_password("kashida")
    user.save()
    return user


@api_view(['POST', 'GET'])
@reversion.create_revision()
def create_client(request):
    try:
        if request.method == 'GET':
            client = ClientProfile.objects.all()
            paginator = CustomPagination()
            paginator.page_size = request.GET.get('per_page')
            paginator.page = request.GET.get('page')
            resources = paginator.paginate_queryset(client, request)
            serializer = ClientSerializer(resources, many=True)
            return paginator.get_paginated_response(serializer.data)

        if request.method == 'POST':
            user = creat_user()
            client = ClientProfile.objects.create(
                user=user,
                name="Kashif",
                phone="03244897133",
            )
            client.save()
            return Response({"success": True})
    except Exception as e:
        print(e)
        return Response({"Message": e})


@api_view(['PUT'])
@reversion.create_revision()
def update_client(request):
    try:
        data = request.data
        client = ClientProfile.objects.get(id=data['id'])
        serializer = ClientSerializer(client, data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True})
        print(serializer.errors)
        return Response({"success": True})
    except Exception as e:
        return Response({"success": True})


@api_view(['GET'])
def check_reversion(request):
    try:
        client = ClientProfile.objects.get(id=10)
        print(client.name)
        obj = Version.objects.get_for_object_reference(ClientProfile, 10)
        return Response({"success": True, "value": obj.values()})
    except Exception as e:
        return Response({"success": False, "Message": e})
