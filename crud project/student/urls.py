from django.urls import path
from .import views

urlpatterns = [
    path('', views.add_show, name="addandshow"),
    path('delete/<str:pk>/', views.delete_data, name="deletedata"), 
    path('update/<str:pk>/', views.update_data, name="updatedata")
]