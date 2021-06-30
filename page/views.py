from django.views.generic import  TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class Product(TemplateView):
    template_name = 'products.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class About(TemplateView):
    template_name = 'about.html'

class About(TemplateView):
    template_name = 'about.html'