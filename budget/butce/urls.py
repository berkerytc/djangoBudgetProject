from django.urls import path
from . import views


urlpatterns = [
    path('',views.transaction_list, name = "transactions"),
    path('add-transaction',views.add_transaction,name="add-transaction"),
    path('edit-transaction/<int:id>', views.edit_transaction,name = "edit-transaction"),
    path('delete-transaction/<int:id>', views.delete_transaction,name= "delete-transaction"),
    path('filter-page', views.filter_page, name= "filter-page"),
]