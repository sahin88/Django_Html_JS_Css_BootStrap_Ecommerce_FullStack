from .views import store, card, checkout, updateItem, processOrder, cardView
from django.urls import path


urlpatterns = [
    path('', store, name="store"),
    path('card/', card, name="card"),
    path('checkout/', checkout, name="checkout"),
    path('update_Item/', updateItem, name="updt-itm"),
    path('process_order/', processOrder, name="process-order"),
    path('card_view/<int:prod_id>/', cardView, name="card_view")
]
