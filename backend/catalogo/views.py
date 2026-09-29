from django.http import JsonResponse
from .models import Servicio

def servicio_list(request):
    """Devuelve en JSON los servicios activos."""
    servicios = list(
        Servicio.objects.filter(activo=True).values(
            "id", "nombre", "descripcion", "precio"
        )
    ) 
    
    return JsonResponse({"count": len(servicios), "results": servicios})