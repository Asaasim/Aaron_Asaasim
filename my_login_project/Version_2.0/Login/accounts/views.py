from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



# @method_decorator(csrf_exempt, name='dispatch')
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = UserLoginForm
    success_url = reverse_lazy('landing_page')

def login_view(request):
    # ... existing code ...
    return render(request, 'accounts/login.html')

def landing_page(request):
    return render(request, 'accounts/landing_page.html')