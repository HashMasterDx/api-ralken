from api.models import LogSolicitud


def get_client_ip_address(request):
    req_headers = request.META
    x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for_value:
        ip_addr = x_forwarded_for_value.split(',')[-1].strip()
    else:
        ip_addr = req_headers.get('REMOTE_ADDR')
    return ip_addr


class LoggingMiddleware:
    def __init__(self, get_response):
        self.META = None
        self.get_response = get_response

    def __call__(self, request):
        # Registra la solicitud en la base de datos
        LogSolicitud.objects.create(
            host=get_client_ip_address(request),
            solicitud=request.path
        )

        # Continúa con la cadena de middlewares y las vistas
        response = self.get_response(request)

        return response

