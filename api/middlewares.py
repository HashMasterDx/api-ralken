from api.models import LogSolicitud

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Registra la solicitud en la base de datos
        LogSolicitud.objects.create(
            host=request.META.get('REMOTE_ADDR'),
            solicitud=request.path
        )

        # Continúa con la cadena de middlewares y las vistas
        response = self.get_response(request)

        return response