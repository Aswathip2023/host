from datetime import timedelta
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Booking, Category, Service, Gallery
from ShoppingApp.models import Product
from .forms import BookingForm
from django.urls import reverse
from WeddingApp.forms import UserRegistrationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_PRIVATE_KEY
from cart.models import CartItem, Cart
from cart.views import _cart_id
# Create your views here.

def payment(request,id,cart_items=None):
    print(id)
    # total=Product.objects.filter(id=id).values('price').get()['price']

    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(user=request.user, cart=cart, active=True)
    price = sum(item.product.price * item.quantity for item in cart_items)
    total=int(price*100)
    print(total)
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'unit_amount': total,
                'product_data':{
                    'name':'Your cart'
                },

            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('demo')),
    )
    context = {
        'session_id':session.id,
        'stripe_public_key':settings.STRIPE_PUBLIC_KEY,
        'user':user,
        'total':total
    }
    return render(request,'service/payment.html',context)

def thanks(request):
    return render(request, 'service/thanks.html')

from .forms import BookingForm

def register(request):
  form = CustomUserCreationForm()
  if request.method == 'POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return render(request, 'login.html')
  return render(request, "register.html", {'form': form,})

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials!!!")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')


def user(request):
    if request.user.is_authenticated:
        apptmnt_info = Appointment.objects.filter(user=request.user)
        return render(request, "user.html",{
            'info': apptmnt_info,
        })
    return redirect('login')


########Sevices##########

def demo(request):
    obj = Category.objects.all()
    return render(request, "index.html", {'category': obj})


def bridal(request):
    bridal = Service.objects.filter(category_id=1)
    return render(request, "services/bridal.html", {'list': bridal})





def makeover(request):
    mkup = Service.objects.filter(category_id=6)
    return render(request, "services/makeover.html", {'list5': mkup})




def gallery(request):
    gallery = Gallery.objects.all
    return render(request, "gallery.html", {'photos': gallery})

def user_details(request):
    return render(request, "service/user_details.html")


########Appointment##########


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            service=form.cleaned_data['service']
            contact = form.cleaned_data['contact ']
            booking_date = form.cleaned_data[' booking_date']
            booked_on = form.cleaned_data['booked_on']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            count = form.cleaned_data['count ']
            description = form.cleaned_data['description ']
            booking.save()
            messages.info(request, 'New booking added successfully')
            booking_info=Booking.objects.filter()
            return render(request, 'my_bookings.html',{
                 'service':service,
                 'contact':contact,
                 'booking_date':booking_date,
                 'booked_on':booked_on,
                 'check_in':check_in,
                 'check_out':check_out,
                 'count':count,
                 'description':description,
            })
    else:
        form=BookingForm
    return render(request,'booking.html',{'form':form})

def appointment_info(request):
    if request.user.is_authenticated:
        # apptmnt_info = Booking.objects.filter(user=request.user)
        return render(request, "booking_info.html", {
            # 'info': apptmnt_info,
        })
    return redirect('appointment')


# CRUD OPERATIONS
def Delete(request, id):
    apptmnt_info = Booking.objects.filter(id=id)
    apptmnt_info.delete()
    messages.info(request, "Appointment Deleted!!!")
    return redirect("appointment_info")


def new(request):
    return render(request, "new.html")
def my_profile(request):
    return render(request, "my_profile.html")
def success(request):
    return render(request, "success.html")

