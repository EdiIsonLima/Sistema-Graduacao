from django.urls import path
from .views import InicioView, ModalidadeListView, PlanoListView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('modalidades/', ModalidadeListView.as_view(), name='lista_modalidades'),
    path('planos/', PlanoListView.as_view(), name='lista_planos'),
]