from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='booking/login.html',
        redirect_authenticated_user=True
    ), name='login'),
]

