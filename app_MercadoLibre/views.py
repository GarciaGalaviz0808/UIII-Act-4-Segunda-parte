from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendedor
# app_MercadoLibre/views.py (añadir estas funciones)
from .models import Categoria

# Agregar categoria (form simple POST)
def agregar_categoria(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "")
        descripcion = request.POST.get("descripcion", "")
        tipo = request.POST.get("tipo", "")
        img_url = request.POST.get("img_url", "")
        activa = True if request.POST.get("activa") == "on" else False

        Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            tipo=tipo,
            img_url=img_url,
            activa=activa
        )
        return redirect("ver_categoria")
    return render(request, "categoria/agregar_categoria.html")

# Ver categorias (lista en tabla)
def ver_categoria(request):
    categorias = Categoria.objects.all().order_by("-fecha_creacion")
    return render(request, "categoria/ver_categoria.html", {"categorias": categorias})

# Mostrar formulario para actualizar
def actualizar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    return render(request, "categoria/actualizar_categoria.html", {"categoria": categoria})

# Realizar actualización (POST)
def realizar_actualizacion_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    if request.method == "POST":
        categoria.nombre = request.POST.get("nombre", categoria.nombre)
        categoria.descripcion = request.POST.get("descripcion", categoria.descripcion)
        categoria.tipo = request.POST.get("tipo", categoria.tipo)
        categoria.img_url = request.POST.get("img_url", categoria.img_url)
        categoria.activa = True if request.POST.get("activa") == "on" else False
        categoria.save()
        return redirect("ver_categoria")
    return redirect("actualizar_categoria", id_categoria=id_categoria)

# Borrar — confirmar y eliminar
def borrar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    if request.method == "POST":
        categoria.delete()
        return redirect("ver_categoria")
    return render(request, "categoria/borrar_categoria.html", {"categoria": categoria})


# Página de inicio del sistema
def inicio_mercadolibre(request):
    contexto = {}
    return render(request, "inicio.html", contexto)

# Agregar vendedor (form simple POST)
def agregar_vendedor(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "")
        apellido = request.POST.get("apellido", "")
        email = request.POST.get("email", "")
        telefono = request.POST.get("telefono", "")
        direccion = request.POST.get("direccion", "")
        ciudad = request.POST.get("ciudad", "")
        # No validamos (según tu pedido)
        Vendedor.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            direccion=direccion,
            ciudad=ciudad
        )
        return redirect("ver_vendedor")
    return render(request, "vendedor/agregar_vendedor.html")

# Ver vendedores (lista en tabla)
def ver_vendedor(request):
    vendedores = Vendedor.objects.all().order_by("-fecha_registro")
    return render(request, "vendedor/ver_vendedor.html", {"vendedores": vendedores})

# Actualizar — muestra formulario con datos
def actualizar_vendedor(request, id_vendedor):
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    return render(request, "vendedor/actualizar_vendedor.html", {"vendedor": vendedor})

# Realizar actualización (POST)
def realizar_actualizacion_vendedor(request, id_vendedor):
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    if request.method == "POST":
        vendedor.nombre = request.POST.get("nombre", vendedor.nombre)
        vendedor.apellido = request.POST.get("apellido", vendedor.apellido)
        vendedor.email = request.POST.get("email", vendedor.email)
        vendedor.telefono = request.POST.get("telefono", vendedor.telefono)
        vendedor.direccion = request.POST.get("direccion", vendedor.direccion)
        vendedor.ciudad = request.POST.get("ciudad", vendedor.ciudad)
        vendedor.save()
        return redirect("ver_vendedor")
    return redirect("actualizar_vendedor", id_vendedor=id_vendedor)

# Borrar — confirmar y eliminar
def borrar_vendedor(request, id_vendedor):
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    if request.method == "POST":
        vendedor.delete()
        return redirect("ver_vendedor")
    return render(request, "vendedor/borrar_vendedor.html", {"vendedor": vendedor})