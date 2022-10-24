from django.urls import path
from api.views import CategoryView,ProductsView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("categories",CategoryView,basename="category")
router.register("products",ProductsView,basename="products")


urlpatterns=[

]+router.urls