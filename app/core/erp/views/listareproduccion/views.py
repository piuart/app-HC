from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ListaReproduccionForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.youtube.models import ListaReproduccion

class ListaReproduccionListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = ListaReproduccion
    template_name = 'listareproduccion/list.html'
    permission_required = 'view_listareproduccion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in ListaReproduccion.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Video'
        context['create_url'] = reverse_lazy('erp:listareproduccion_create')
        context['list_url'] = reverse_lazy('erp:listareproduccion_list')
        context['entity'] = 'Videos'
        return context


class ListaReproduccionCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = ListaReproduccion
    form_class = ListaReproduccionForm
    template_name = 'listareproduccion/create.html'
    success_url = reverse_lazy('erp:listareproduccion_list')
    permission_required = 'add_listareproduccion'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un Video'
        context['entity'] = 'Videos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ListaReproduccionUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = ListaReproduccion
    form_class = ListaReproduccionForm
    template_name = 'listareproduccion/create.html'
    success_url = reverse_lazy('erp:listareproduccion_list')
    permission_required = 'change_listareproduccion'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un Video'
        context['entity'] = 'Videos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ListaReproduccionDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = ListaReproduccion
    template_name = 'listareproduccion/delete.html'
    success_url = reverse_lazy('erp:listareproduccion_list')
    permission_required = 'delete_listareproduccion'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un Video'
        context['entity'] = 'Videos'
        context['list_url'] = self.success_url
        return context

