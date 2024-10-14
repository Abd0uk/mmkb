from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home.html')  # Make sure to create 'home.html' template


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Path to your login template
    redirect_authenticated_user = True  # Redirect if user is already authenticated
    next_page = reverse_lazy('home')  # Redirect to this URL after login (change 'home' to your desired view)
    
    # Optional: You can add extra context or modify the behavior here
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'  # Example of passing extra context to the template
        return context




