from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Supplier, Stock
from .forms import ProductForm, SupplierForm, StockForm


# =========================
# PRODUCT
# =========================

def product_list(request):
    products = Product.objects.all()

    low_stock_products = Product.objects.filter(quantity__lte=10)

    return render(request, "product_list.html", {
        "products": products,
        "low_stock_products": low_stock_products,
    })

def add_product(request):
    suppliers = Supplier.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        price = request.POST['price']
        quantity = request.POST['quantity']
        supplier_id = request.POST['supplier']

        Product.objects.create(
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            supplier_id=supplier_id
        )

        return redirect('product_list')

    return render(request, 'add_product.html', {
        'suppliers': suppliers
    })

def edit_product(request, id):

    product = get_object_or_404(Product, id=id)
    suppliers = Supplier.objects.all()

    if request.method == "POST":

        product.name = request.POST["name"]
        product.category = request.POST["category"]
        product.price = request.POST["price"]
        product.quantity = request.POST["quantity"]
        product.supplier_id = request.POST["supplier"]

        product.save()

        return redirect("product_list")

    return render(request, "edit_product.html", {
        "product": product,
        "suppliers": suppliers
    })

def delete_product(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "delete_product.html", {
        "product": product
    })


# =========================
# SUPPLIER
# =========================

def supplier_list(request):

    suppliers = Supplier.objects.all()

    return render(request, "supplier_list.html", {
        "suppliers": suppliers
    })


def add_supplier(request):

    if request.method == "POST":

        form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("supplier_list")

    else:
        form = SupplierForm()

    return render(request, "add_supplier.html", {
        "form": form
    })


def edit_supplier(request, id):

    supplier = Supplier.objects.get(id=id)

    if request.method == "POST":

        supplier.name = request.POST["name"]
        supplier.email = request.POST["email"]
        supplier.phone = request.POST["phone"]
        supplier.address = request.POST["address"]

        supplier.save()

        return redirect("supplier_list")

    return render(request, "edit_supplier.html", {
        "supplier": supplier
    })


def delete_supplier(request, id):

    supplier = get_object_or_404(Supplier, id=id)

    if request.method == "POST":
        supplier.delete()
        return redirect("supplier_list")

    return render(request, "delete_supplier.html", {
        "supplier": supplier
    })


# =========================
# STOCK
# =========================
def stock_list(request):
    stocks = Stock.objects.all()

    search = request.GET.get('search')

    if search:
        stocks = stocks.filter(
            product__name__icontains=search
        )

    return render(request, 'stock_list.html', {
        'stocks': stocks
    })

def add_stock(request):

    if request.method == "POST":

        form = StockForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("stock_list")

    else:
        form = StockForm()

    return render(request, "add_stock.html", {
        "form": form
    })



def edit_stock(request, id):

    stock = get_object_or_404(Stock, id=id)

    if request.method == "POST":

        stock.quantity = request.POST["quantity"]

        stock.save()

        return redirect("stock_list")

    return render(request, "edit_stock.html", {
        "stock": stock
    })


def delete_stock(request, id):

    stock = get_object_or_404(Stock, id=id)

    if request.method == "POST":
        stock.delete()
        return redirect("stock_list")

    return render(request, "delete_stock.html", {
        "stock": stock
    })