from page import views
from page.views import *
from django.urls import path


app_name = 'myapp'

urlpatterns = [
    path('about', About.as_view(), name='about'),
    path('contact', Contact.as_view(), name='contact'),
    path('product', Product.as_view(), name='product')

]