from django.urls import path
from customer import views
from customer.views import addtowishlist

urlpatterns=[
    path("",views.LoginView.as_view(),name="login"),
    path("register",views.RegistrationView.as_view(),name="registration"),
    path("home",views.HomeView.as_view(),name="home"),
    path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("products/<int:id>/carts/add",views.AddToCartView.as_view(),name="addto-cart"),
    path("products/carts/all",views.MyCartView.as_view(),name="MyCart"),
    path("carts/placeorder/<int:cid>/<int:pid>",views.PlaceOrderView.as_view(),name="place_order"),
    path("products/categories/<int:id>",views.CategoryListView.as_view(),name="category-list"),
    path("logout",views.SignOutView.as_view(),name="signout"),
    path("products/<int:id>/wishlist/add",addtowishlist,name="wishlist"),
    path("products/wishlists/all",views.MyWishlistView.as_view(),name="mywishlist")

]