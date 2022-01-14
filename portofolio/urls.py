from django.urls import path

from . import views

app_name = 'portofolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('test/', views.test_page_view, name='test'),
]
