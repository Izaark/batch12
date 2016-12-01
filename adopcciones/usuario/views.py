from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView
from django.core.urlresolvers import reverse_lazy
from .models import Usuario
from .forms import RegisterForm

class RegistrarUsuarioCreateView(CreateView):
    model = Usuario
    template_name = "registrar.html"
    form_class = RegisterForm
    success_url = reverse_lazy('usuario:listado_usuarios')

class UsuarioListView(ListView):
    model = Usuario
    template_name = "usuario/usuario_list.html"
    paginate_by = 3