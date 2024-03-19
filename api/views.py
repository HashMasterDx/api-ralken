import os
import requests
import geoip2.database
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import UserSerializer, BitacoraSerializer
from api.models import User, LogSolicitud
from django.conf import settings


@extend_schema_view(
    list=extend_schema(summary="List all users"),
    retrieve=extend_schema(summary="Retrieve a user"),
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema_view(
    list=extend_schema(summary="Listar Solicitudes"),
)
class BitacoraViewSet(viewsets.ModelViewSet):
    queryset = LogSolicitud.objects.all()
    serializer_class = BitacoraSerializer


# Obtener usuarios
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@extend_schema(
    description="Obtener todos los usuarios",
    responses={200: dict(description="Lista de usuarios")},
    tags=["Usuarios"],
)
def obtener_usuarios(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "No se pudo obtener los usuarios"}, status=500)


# Obtener albumes
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@extend_schema(
    description="Obtener Albumes",
    responses={200: dict(description="Lista de albumes")},
    tags=["Albumes"],
)
def obtener_albumes(request, userId=None):
    if userId is None:
        response = requests.get("https://jsonplaceholder.typicode.com/albums")
    else:
        response = requests.get(f"https://jsonplaceholder.typicode.com/albums?userId={userId}")

    if response.status_code == 200:
        return Response(response.json())
    else:
        return Response({"error": "No se pudo obtener los albumes"}, status=500)


# Obtener posts
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@extend_schema(
    description="Obtener Posts",
    responses={200: dict(description="Lista de posts")},
    tags=["Posts"],
)
def obtener_posts(request, userId=None):
    if userId is None:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
    else:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={userId}")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "No se pudo obtener los posts"}, status=500)


# Obtener comentarios
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@extend_schema(
    description="Obtener todos los comentarios",
    responses={200: dict(description="Lista de comentarios")},
    tags=["Comentarios"],
)
def obtener_comentarios(request, postId=None):
    if postId is None:
        response = requests.get("https://jsonplaceholder.typicode.com/comments")
    else:
        response = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={postId}")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "No se pudo obtener los comentarios"}, status=500)


# Obtener fotos
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@extend_schema(
    description="Obtener todas las fotos",
    responses={200: dict(description="Lista de fotos")},
    tags=["Fotos"],
)
def obtener_fotos(request, albumId=None):
    if albumId is None:
        response = requests.get("https://jsonplaceholder.typicode.com/photos")
    else:
        response = requests.get(f"https://jsonplaceholder.typicode.com/photos?albumId={albumId}")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "No se pudo obtener las fotos"}, status=500)


def get_country_info(ip_address):
    # Path to the GeoIP2 database
    geoip_path = os.path.join(settings.BASE_DIR, 'GeoLite2-City.mmdb')    # Initialize GeoIP2 reader
    reader = geoip2.database.Reader(geoip_path)

    try:
        # Lookup the IP address
        response = reader.city(ip_address)

        # Get country information
        country_code = response.country.iso_code
        country_name = response.country.name

        return country_code, country_name
    except geoip2.errors.AddressNotFoundError:
        return None, None
    finally:
        reader.close()