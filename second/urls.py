from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home' ),
    path('delete_item/<int:tid>/',views.delete_item ),
    path('edit/<int:tid>/',views.edit),
]