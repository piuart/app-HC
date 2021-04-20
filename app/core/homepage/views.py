# Create your views here.
from datetime import datetime

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from core.youtube.models import ListaReproduccion

class IndexView(TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        return 'index.html'

    def get(self, request, *args, **kwargs):
        action = request.GET['action'] if 'action' in request.GET else ''
        if action == 'mostrarvideos':
            try:
                fechaactual = datetime.now().date()
                hora = datetime.now().time()
                horamin = "{}:00".format(datetime.now().strftime('%M:%S'))
                print(horamin)
                lista = ListaReproduccion.objects.filter(fecha_subida=fechaactual, hora_subida__icontains=horamin).first()
                if lista:
                    return JsonResponse({'resp': True, 'idvideo': lista.idvideo, 'hora': hora, 'nombre': lista.nombre})
                else:
                    return JsonResponse({'resp': False})
            except Exception as ex:
                return JsonResponse({'resp': False})
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        context['namesala'] = 'videos'
        fechaactual = datetime.now().date()
        context['listareproduccion'] = ListaReproduccion.objects.filter(fecha_subida=fechaactual).order_by('fecha_subida', 'hora_subida')
        context['hoy'] = fechaactual
        return context
