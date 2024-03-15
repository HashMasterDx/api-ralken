from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

from api.views import UserViewSet, BitacoraViewSet

router: ExtendedSimpleRouter = ExtendedSimpleRouter()

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"bitacora", BitacoraViewSet)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/swagger/", SpectacularSwaggerView.as_view(url_name="api:schema"), name="swagger"),
    path("usuarios/", views.obtener_usuarios, name="obtener_usuarios"),
    path("albumes/", views.obtener_albumes, name="obtener_albumes"),
    path("albumes/<int:userId>/", views.obtener_albumes, name="obtener_albumes_user"),
    path("posts/", views.obtener_posts, name="obtener_posts"),
    path("posts/<int:userId>/", views.obtener_posts, name="obtener_posts_user"),
    path("comments/", views.obtener_comentarios, name="obtener_comentarios"),
    path("comments/<int:postId>/", views.obtener_comentarios, name="obtener_comentarios_post"),
    path("photos/", views.obtener_fotos, name="obtener_fotos"),
    path("photos/<int:albumId>/", views.obtener_fotos, name="obtener_fotos_album"),
    path("", include(router.urls)),
]