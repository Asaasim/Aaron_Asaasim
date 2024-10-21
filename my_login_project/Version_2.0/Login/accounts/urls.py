from django.urls import path
from .views import CustomLoginView, landing_page
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
    path('landing-page/', views.landing_page, name='landing_page'),  # Landing page URL
]