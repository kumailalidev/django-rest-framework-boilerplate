from rest_framework import status
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(http_method_names=["GET"])
def ping(request: HttpRequest):
    return Response(data={"ping": "pong"}, status=status.HTTP_200_OK)
