#main registry for our apis 
# if we have additonal apps we bring them here and register them 
from rest_framework.routers import DefaultRouter
from django.urls import path, include 
from customers.api.urls import customer_router


router = DefaultRouter()

#app1
#app1
#customers
router.registry.extend(customer_router.registry)

urlpatterns = [
    path('', include(router.urls)),

]