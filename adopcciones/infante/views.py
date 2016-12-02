from django.views.generic  import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import InfanteForm
from .models import Infante

class InfanteListView(ListView):
    model = Infante
    template_name = "infante/infante_list.html"
    paginate_by = 2

class InfanteCreateView(CreateView):
	model = Infante
	form_class = InfanteForm
	template_name = 'infante/infante_forms.html'
	success_url = reverse_lazy('infante:infante_listar')

class InfanteUpdateView(UpdateView):
	model = Infante
	form_class = InfanteForm
	template_name = 'infante/infante_forms.html'
	success_url = reverse_lazy('infante:infante_listar')

class InfanteDeleteView(DeleteView):
	model = Infante
	template_name = 'infante/infante_delete.html'
	success_url = reverse_lazy('infante:infante_listar')