from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required, permission_required 
from .models import Categoria, Producto
from .forms import ProductoForm, CustomUserCreationForm
from StreetShopKid import urls

# Create your views here.
def index(request):
    template_name="index.html"
    categorias=Categoria.objects.filter(activo=True)
    productos=Producto.objects.filter(activo=True)
    context = {"productos":productos,"categorias":categorias}
    return render(request, template_name,context)

def buscar_categoria(request, slug):
    template_name="list.html"
    cat=Categoria.objects.get(slug=slug)
    categorias=Categoria.objects.filter(activo=True)
    productos=Producto.objects.filter(activo=True, categoria=cat)
    context = {"productos":productos,"categorias":categorias}
    return render(request, template_name,context)

def search(request):
    template_name = "list.html"
    q=request.GET["q"]
    productos=Producto.objects.filter(activo=True, nombre__icontains=q)
    categorias=Categoria.objects.filter(activo=True)
    context = {"productos":productos,"categorias":categorias}
    return render(request, template_name,context)

def detail(request, slug):
    if Producto.objects.filter(activo=True, slug=slug).exists():
        template_name = "detail.html"
        productos=Producto.objects.filter(activo=True, slug=slug)
        categorias=Categoria.objects.filter(activo=True)
        context = {"productos":productos,"categorias":categorias}
        return render(request, template_name,context)
        
def carro(request):
    template_name="carro.html"
    categorias=Categoria.objects.filter(activo=True)
    productos=Producto.objects.filter(activo=True)
    context = {"productos":productos,"categorias":categorias}
    return render(request, template_name,context)

def micarro(request):
    template_name="carro.html"
    categorias=Categoria.objects.filter(activo=True)
    productos=Producto.objects.filter(activo=True)
    context = {"productos":productos,"categorias":categorias}
    return render(request, template_name,context)

@permission_required('StreetShopKidApp.add_producto')
def agregarProducto(request):
    template_name="producto/agregar.html"
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado Correctamente")
    return render(request, template_name, data)
@permission_required('StreetShopKidApp.view_producto')
def listarProductos(request):
    template_name="producto/listar.html"
    productos=Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':productos,
        'paginator': paginator
    }
    return render(request, template_name, data)
@permission_required('StreetShopKidApp.change_producto')
def modificarProducto(request, id):
    template_name="producto/modificar.html"
    productoo = get_object_or_404(Producto, codigo=id)

    data = {
        'form': ProductoForm(instance = productoo)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=productoo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Con Exito")
            return redirect(to="listarProducto")
    return render(request, template_name, data)
@permission_required('StreetShopKidApp.delete_producto')
def eliminarProducto(request, id):
    productoo = get_object_or_404(Producto, codigo=id)
    productoo.delete()
    messages.success(request, "Producto Eliminado")
    return redirect(to="listarProducto")


def registro(request):
    template_name="registration/registro.html"
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro de Usuario Correcto")
            return redirect(to="index")
            
    return render(request, template_name, data)

