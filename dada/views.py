from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.views import LogoutView
from django.contrib.auth import get_user_model

from .forms import SignUpForm
from .models import CustomUser

User = get_user_model()

# HOME VIEW
@method_decorator(never_cache, name='dispatch')
class Home(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'index.html'
    context_object_name = 'userdata'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Dashboard Home'
        return context

# LOGIN VIEW
class CustomLoginView(FormView):
    template_name = 'user_page/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, "Invalid credentials. Please try again.")
            return self.form_invalid(form)

# SIGNUP VIEW
class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'user_page/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

# USERDATA VIEW
class userdata(ListView):
    model = CustomUser
    template_name = 'userdata.html'
    context_object_name = 'userdata'

# LOGOUT VIEWS
class LogoutConfirmView(TemplateView):
    template_name = 'your_logout_confirmation_template.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'
