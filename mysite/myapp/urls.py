from .views import index,edit,delete
from django.urls import path

urlpatterns = [
    path('',index,name="index"),
    path('edit/<int:id>/',edit,name="edit"),
    path("delete/<int:id>/",delete,name="delete"),
]
