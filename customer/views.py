from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from owner.models import Products,Carts,Orders,Categories,Wishlist,Enquiry

# Create your views here.
from django.views.generic import CreateView,TemplateView,FormView,DetailView,ListView,View
from customer import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from customer.decorators import signin_required
from django.contrib import messages
from django.core.mail import send_mail


# def error_404_view(request,exception):
#     return render(request,'404.html')
#
# def error_400_view(request,exception):
#     return render(request,'400.html')
#
# def error_403_view(request,exception):
#     return render(request,'403.html')
#
# def error_500_view(request):
#     return render(request,'500.html')


class RegistrationView(CreateView):
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)

class LoginView(FormView):
    form_class = forms.LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request, "login successful")
                if request.user.is_superuser:
                    return redirect("dashboard")
                else:
                    return redirect("home")
            else:
                messages.error(request, "invalid credentials")
                return render(request, "login.html", {"form": form})
        else:
            messages.error(request, "invalid credentials")
            return render(request,"login.html",{"form":form})


# @method_decorator(signin_required,name="dispatch")
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_products=Products.objects.all()
        all_categories=Categories.objects.all()
        context["products"]=all_products
        context["categories"]=all_categories
        return context

@method_decorator(signin_required,name="dispatch")
class CategoryListView(ListView):
    model = Products
    context_object_name = "categories"
    template_name = "categories-list.html"





@method_decorator(signin_required,name="dispatch")
class ProductDetailView(DetailView):
    template_name = "product-detail.html"
    model = Products
    context_object_name = "product"
    pk_url_kwarg = "id"




@method_decorator(signin_required,name="dispatch")
class AddToCartView(FormView):
    template_name = "addto-cart.html"
    form_class = forms.CartForm

    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        return render(request,self.template_name,{"form":forms.CartForm(),"product":product})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        product = Products.objects.get(id=id)
        qty=request.POST.get("qty")
        user=request.user
        Carts.objects.create(product=product,user=user,qty=qty)
        return redirect("home")


@method_decorator(signin_required,name="dispatch")
class MyCartView(ListView):
    model = Carts
    template_name = "cart-list.html"
    context_object_name = "carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-created_date")


@method_decorator(signin_required,name="dispatch")
class PlaceOrderView(FormView):
    template_name = "place_order.html"
    form_class = forms.OrderForm

    def post(self, request, *args, **kwargs):
        cart_id=kwargs.get("cid")
        product_id=kwargs.get("pid")
        cart=Carts.objects.get(id=cart_id)
        product=Products.objects.get(id=product_id)
        user=request.user
        delivery_address=request.POST.get("delivery_address")
        Orders.objects.create(product=product,user=user,delivery_address=delivery_address)
        cart.status="order-placed"
        cart.save()

        return redirect("home")


@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")


# @method_decorator(signin_required,name="dispatch")
def addtowishlist(request,*args,**kwargs):
    id = kwargs.get("id")
    product = Products.objects.get(id=id)
    user = request.user
    Wishlist.objects.create(product=product, user=user)
    messages.success(request,"success")
    return redirect("home")


@method_decorator(signin_required,name="dispatch")
class MyWishlistView(ListView):
    model = Wishlist
    template_name = "wishlist.html"


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_products=Products.objects.all()
        all_wishlist=Wishlist.objects.all()
        context["products"]=all_products
        context["wishlist"]=all_wishlist
        return context

class EnquiryView(FormView):
    form_class = forms.EnquiryForm
    template_name = "enquiry.html"

    def post(self, request, *args, **kwargs):
        form=forms.EnquiryForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            email=form.cleaned_data.get("email")
            message=form.cleaned_data.get("message")
            form.save()

            send_mail(
                'Subject here',
                'Here is the message.',
                'sivajyothis9446@gmail.com',
                ['isivajyothis@gmail.com'],

            )





