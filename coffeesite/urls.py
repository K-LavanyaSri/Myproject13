from django.urls import path
from .views import *
app_name='coffeesite'

urlpatterns = [
    path('',home,name='home'),
    path('products/',products,name='products'),
    # path('testimonials/',testimonials,name='testimonials'),
    # path('aboutUs/',aboutUs,name='aboutUs'),
    # path('contactUs/',contactUs,name='contactUs'),
]
