from django.urls import path

from repository import views

urlpatterns = [
    path('', views.CatalogueView.as_view(), name='catalogue'),
]