from django.urls import include, path
from .views import *

# define the router path and viewset to be used


# specify URL Path for rest_framework
urlpatterns = [

       # Vendor Page
       path('vendors', Vendoradd.as_view()),
       path('vendors/<int:id>',Vendordatasget.as_view()),

       # PO Page
       path('purchase_orders',Purchaseorderadd.as_view()),
       path('purchase_orders/<int:id>',POdatasget.as_view()),
       path('purchase_orders/<int:id>/acknowledge',Acknowledge_update.as_view()),

       #Performnce Matrix
       path('vendors/<int:id>/performance',Performance_matrix.as_view())

]
