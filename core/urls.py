from django.contrib import admin
from django.urls import path
from siteapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('wisc/', views.wisc, name='wisc'),
    path('planos/', views.planos, name='planos'),
    path('login/', views.login_register, name='login_register'),
    path('laudos/', views.index_page, name='index_page'),
]
