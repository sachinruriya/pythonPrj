from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,UserRegistrationForm,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


def upload_profile(request):
    if request.method == "POST":
       age = request.POST['age']
       image = request.FILES['profile']
       Profile.objects.create(age=age,image=image)

    return render(request, 'dashboard.html')   

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
        
    else:
        form = UserRegistrationForm()


    return render(request, 'registration/register.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        userd = User.objects.filter(username=username)
        if userd:
            userv = authenticate(username=username,password=password)
            if userv:
                login(request,userv)
                return redirect("dashboard")
    return render(request,"registration/login.html")


@login_required
def dashboard(request):
    print(request.user.id)
    user_id = request.user.id
    orders = Profile.objects.select_related('user').filter(user_id=user_id)
    return render(request, 'dashboard.html',{'orders':orders})

@login_required
def createProduct(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Product.objects.create(name=name,description=description,price=price)
        return redirect('list_product')
    return render(request,'create_prd.html')

def list_product(request):
    product = Product.objects.all()
    return render(request,"list_products.html",{"products":product})

def editProduct(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == "POST":
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect('list_product')
    return render(request, 'update_product.html', {'product': product})

def deleteProduct(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('list_product')
    return render(request, 'delete_product.html', {'product': product})

    
# Create your views here.
