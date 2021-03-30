from django.shortcuts import render
from store.models.customer import Customer

def demo(request):
    pictures = Customer.objects.all()
    ctx = {'pictures': pictures}
    return render(request, 'demo.html', ctx)