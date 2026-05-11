from django.urls import path
from .views import InicioView, ModalidadeListView, PlanoListView

urlpatterns = [
    
    path('', InicioView.as_view(), name='inicio'),
    path('planos/', PlanoListView.as_view(), name='lista_planos'),

]