from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpRequest


@api_view(http_method_names=["GET"])
def ping(request: HttpRequest):
    """
    A view function for handling ping requests.

    This function responds to HTTP GET requests by returning a JSON response
    with a "pong" message, indicating that the server is up and running.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: A JSON response with a "ping" key and "pong" value.
    """
    # Create a JSON response with a "ping" key and "pong" value
    response_data = {"ping": "pong"}
    # Return the response with HTTP status code 200 OK
    return Response(data=response_data, status=status.HTTP_200_OK)
