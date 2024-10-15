from django.urls import path
from .views import home, login, register, alltodos, deleteItem, updateItem

urlpatterns = [
    path('', home, name='home'), 
    path('login/',login, name='login'),          # Added trailing slash
    path('registration/', register, name='register'), # Added trailing slash
    path('alltodo/', alltodos, name='alltodos'),  # Added trailing slash
    path('delete_item/<int:pk>/', deleteItem, name='deleteItem'), # Added trailing slash
    path('update_item/<int:pk>/', updateItem, name='updateItem'), # Added trailing slash
]
