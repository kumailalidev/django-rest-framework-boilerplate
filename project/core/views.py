from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpRequest
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


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

def image_upload(request):
    """
    View function for handling image uploads.

    Args:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: Rendered HTML response.
    """

    # Check if the request method is POST and an image file is included in the request.
    if request.method == "POST" and request.FILES["image_file"]:
        # Get the uploaded image file from the request.
        image_file = request.FILES["image_file"]

        # Initialize a FileSystemStorage object to handle file storage.
        fs = FileSystemStorage()

        # Save the uploaded image file to the file system and get the filename.
        filename = fs.save(image_file.name, image_file)

        # Get the URL of the saved image.
        image_url = fs.url(filename)

        # Print the image URL for debugging purposes.
        print(image_url)

        # Render the upload.html template with the image URL passed as context data.
        return render(request, "core/upload.html", {"image_url": image_url})

    # else if the request method is not POST
    return render(request, "core/upload.html")
