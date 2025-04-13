from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# View to display products and add new ones
def homepage(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Redirect to prevent duplicate submissions
    else:
        form = ProductForm()

    # Get all products in the database
    products = Product.objects.all()

    return render(request, 'items/homepage.html', {'products': products, 'form': form})
