from django.urls import  path
from . import views
# from .views import register
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('create/', views.createProduct , name="createProduct"),
    path('', views.list_product , name="list_product"),
    path('update/<int:product_id>/', views.editProduct , name="editProduct"),
    path('delete/<int:product_id>/', views.deleteProduct , name="deleteProduct"),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/',views.upload_profile , name="profile"),
    path('login/', views.login_page , name="login"),
    path('api/token/', obtain_auth_token, name='api_token_auth'),

]
