from django.urls import path
from . import views



urlpatterns = [
    path('', views.ApiOverview),
    path('all/',views.getData),
    path('add/',views.addItem),
    path('item/<int:pk>/delete/',views.deleteItem),
    path('update/<int:pk>/', views.updateItem)
]