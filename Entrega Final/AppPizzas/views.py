from django.http import HttpResponse
from django.shortcuts import render
from AppPizzas.models import *
from AppPizzas.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#Vista de inicio

def inicioSesion(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password=contra)

            if user:
                login(request,user)
                return render(request,"AppPizzas/inicio.html",{"mensaje":f"Bienvenido {user}"})
            
        else:
            return render(request,"AppPizzas/inicio.html",{"mensaje":"Datos incorrectos."})
        
    else:

        form = AuthenticationForm()

    return render(request,"AppPizzas/login.html",{"formulario":form})

def cerrarSesion(request):
    logout(request)
    return render(request,"AppPizzas/logout.html")

def registro(request):

    if request.method =="POST":

        form =UsuarioRegistro(request.POST)

        if form.is_valid():
            info=form.cleaned_data
            usuario = info["first_name"]
            
            form.save()
            return render(request,"AppPizzas/inicio.html",{"mensaje":"Usuario creado"})
        
    else:

        form = UsuarioRegistro()

    return render(request,"AppPizzas/registro.html",{"formulario":form})

@login_required
def editar_usuario(request):

    usuario_actual = request.user #Se obtiene al usuario actualmente registrado

    if request.method =="POST":

        form =EditarUsuario(request.POST)

        if form.is_valid():
            
            usuario=form.cleaned_data

            usuario_actual.email = usuario["email"]
            
            usuario_actual.first_name = usuario["first_name"]
            usuario_actual.last_name = usuario["last_name"]
            usuario_actual.password1=usuario["password1"]
            usuario_actual.password2=usuario["password2"]
            

            usuario_actual.save()
            return render(request,"AppPizzas/inicio.html")
        
    else:

        form = EditarUsuario(initial={"email":usuario_actual.email})

    return render(request,"AppPizzas/editar_usuario.html",{"formulario":form,"usuario":usuario_actual})



def inicio(request):
    return render(request,"AppPizzas/inicio.html")


def sobremi(request):
    return render(request,"AppPizzas/sobremi.html")

#Vista sobre agregar pizza, creadores y asesores
#@login_required
def agregarPizza(request):

    if request.method=="POST":
        info_formulario = PizzaFormulario(request.POST)
        
        if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            nueva_pizza = Pizza(nombre=info["nombre"],tamaño=info["tamaño"],masa=info["masa"],ingrediente1=info["ingrediente1"],ingrediente2=info["ingrediente2"],ingrediente3=info["ingrediente3"],ingrediente4=info["ingrediente4"])
            nueva_pizza.save()
            return render (request,"AppPizzas/inicio.html")


    else:
        info_formulario = PizzaFormulario()
    return render(request,"AppPizzas/todas_pizzas.html",{"nuevo":info_formulario})

def agregar_asesor(request):
    if request.method=="POST":
        asesor_formulario = AsesorFormulario(request.POST)
        
        if asesor_formulario.is_valid():
            asesor = asesor_formulario.cleaned_data
            datos_asesor = Asesor(nombre=asesor["nombre"],cod_ases=asesor["cod_ases"],correo=asesor["correo"])
            datos_asesor.save()
            return render (request,"AppPizzas/inicio.html")


    else:
        asesor_formulario = AsesorFormulario()
    return render(request,"AppPizzas/asesor.html",{"nuevo_asesor":asesor_formulario})


def agregar_creador(request):
    if request.method=="POST":
        creador_formulario = CreadorFormulario(request.POST)
        
        if creador_formulario.is_valid():
            cread = creador_formulario.cleaned_data
            datos_creador = Creador(nombre=cread["nombre"],edad=cread["edad"],correo=cread["correo"])
            datos_creador.save()
            return render (request,"AppPizzas/inicio.html")
        
    else:
        creador_formulario = CreadorFormulario()
    return render(request,"AppPizzas/creador.html",{"nuevo_creador":creador_formulario})


#Vistas de búsquedas
def verPizza(request):

    return render(request,"AppPizzas/todas_pizzas.html")

def busquedaPizza(request):
    
    return render(request,"AppPizzas/busquedaPizza.html")

def resultados2 (request):
    if request.GET["tamaño"]:

        tamaño = request.GET["tamaño"]
        resultados = Pizza.objects.filter(tamaño__icontains=tamaño)
    
        return render(request,"AppPizzas/resultados.html", {"tamaño":tamaño})
    
    else:
        respuesta="No enviaste datos"

    return HttpResponse(respuesta)

def resultados (request):
    if request.method=='GET':

        tamaño = request.GET["tamaño"]
        resultados = Pizza.objects.filter(tamaño__icontains=tamaño)
    
        return render(request,"AppPizzas/resultados.html", {"resultados":resultados})
    
    else:
        respuesta="No enviaste datos"

    return HttpResponse(respuesta)

#CRUD de Creador
def leerCreador(request):
    creadores = Creador.objects.all()
    contexto = {"cread" : creadores}
    return render(request,"AppPizzas/leerCreador.html", contexto)

def eliminarCreador(request,creadorNombre):
    creador = Creador.objects.get(nombre=creadorNombre)
    creador.delete()

    creadores = Creador.objects.all()

    contexto = {"cread":creadores}
                        
    return render(request,"AppPizzas/leerCreador.html", contexto)

def editarCreador(request,creadorNombre):
    creador = Creador.objects.get(nombre=creadorNombre)

    if request.method == "POST":
        creador_formulario = CreadorFormulario(request.POST)
        
        if creador_formulario.is_valid():
           info = creador_formulario.cleaned_data
           creador.nombre=info["nombre"]
           creador.edad=info["edad"]
           creador.correo=info["correo"]

           creador.save()
           
           return render (request,"AppPizzas/inicio.html")
        
    else:
        creador_formulario = CreadorFormulario(initial={"nombre":creador.nombre,"edad":creador.edad,
                                                        "correo":creador.correo})
    return render(request,"AppPizzas/editarCreador.html",{"nuevo_creador":creador_formulario, 
                                                          "nombre":creadorNombre})
#CRUD con clases -  Pizza
class ListaPizza(LoginRequiredMixin, ListView):
    model = Pizza

class DetallePizza(LoginRequiredMixin,DetailView):
    model = Pizza

class CrearPizza(LoginRequiredMixin,CreateView):
    model = Pizza
    success_url = "/AppPizzas/Pizza/list"
    fields = ["nombre","tamaño","masa","ingrediente1","ingrediente2","ingrediente3","ingrediente4"]

class ActualizarPizza(LoginRequiredMixin,UpdateView):
    model = Pizza
    success_url = "/AppPizzas/Pizza/list"
    fields = ["nombre","tamaño","masa","ingrediente1","ingrediente2","ingrediente3","ingrediente4"]
class BorrarPizza(LoginRequiredMixin, DeleteView):
    model = Pizza
    success_url = "/AppPizzas/Pizza/list"


#CRUD con clases - Creador
class ListaCreador(LoginRequiredMixin, ListView):
    model = Creador

class DetalleCreador(LoginRequiredMixin,DetailView):
    model = Creador

class CrearCreador(LoginRequiredMixin,CreateView):
    model = Creador
    success_url = "/AppPizzas/Creador/list"
    fields = ["nombre","edad","correo"]

class ActualizarCreador(LoginRequiredMixin,UpdateView):
    model = Creador
    success_url = "/AppPizzas/Creador/list"
    fields = ["nombre","edad","correo"]

class BorrarCreador(LoginRequiredMixin, DeleteView):
    model = Creador
    success_url = "/AppPizzas/Creador/list"


#CRUD con clases - Asesor
class ListaAsesor(LoginRequiredMixin, ListView):
    model = Asesor

class DetalleAsesor(LoginRequiredMixin,DetailView):
    model = Asesor

class CrearAsesor(LoginRequiredMixin,CreateView):
    model = Asesor
    success_url = "/AppPizzas/Asesor/list"
    fields = ["nombre","cod_ases","correo"]

class ActualizarAsesor(LoginRequiredMixin,UpdateView):
    model = Asesor
    success_url = "/AppPizzas/Asesor/list"
    fields = ["nombre","cod_ases","correo"]

class BorrarAsesor(LoginRequiredMixin, DeleteView):
    model = Asesor
    success_url = "/AppPizzas/Asesor/list"

