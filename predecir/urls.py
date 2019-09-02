from django.urls import path
from . import  views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('home/',views.dashboardView,name='dashboard'), #Home
    path('',LoginView.as_view(),name='login_url'),
    path('logout/',LogoutView.as_view(next_page='login_url'),name='logout'),
    path('persona/', views.persona_new, name='presona_new'),
    path('consulta/', views.consulta, name='consulta'),
]