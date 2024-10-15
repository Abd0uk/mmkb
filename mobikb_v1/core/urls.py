from django.urls import path
from .views import CustomLoginView, home
from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),  # Add the URL pattern for home
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout URL
    
]
