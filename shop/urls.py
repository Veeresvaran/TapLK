from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('collection/', views.collection, name='collection'),
    path('collection/<str:name>/', views.collectionview, name='collectionview'),
    path('collection/<str:cname>/<str:pname>', views.product_details, name='product_detail'),

]