from django.shortcuts import render
from django.contrib import messages, sessions
#------------------------Para el login
from django import forms
from django.shortcuts import redirect
#.....................................
from .models import Producto
from .models import Cliente

from .models import Cita
from django.core.mail import send_mail
# Create your views here.
#--------------------------------------------------------------Esto debería ir en forms
class LoginForm(forms.Form):
    username= forms.CharField(label=("Nombre de usuario"), required=True, widget=forms.TextInput(attrs={'size': '40'}))
    password= forms.CharField(widget=forms.PasswordInput,required=True,label=("Password"))

class RegistroForm(forms.Form):
    user=forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'size': '40'}))
    nombre=forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'size':'100'}))
    email=forms.EmailField(label="Correo electronico")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput())
class FormContra(forms.Form):
    user=forms.CharField(label="Nombre de usuario",widget=forms.TextInput(attrs={'size':'40'}))
    mail=forms.EmailField(label="Correo electronico")
class AgendarForm(forms.Form):
    hora_inicio= forms.DateTimeField()
    num_paquete=forms.ChoiceField(choices=('1','2','3'))
#--------------------------------------------------------------------------------------

def productos(request):
    productos = Producto.objects.all()
    return render(request,'cuerpo/productos.html',{'productos':productos})
#---------------------------------------------------------------------------------------
def citas(request):
    #Se debe obtener el usuario loggeado y buscar las citas que ha realizado
    citas=[]
    user= request.session['username']
    messages.info(request, user.lower())
    cliente=Cliente.objects.get(user=user.lower())
    todas_citas= Cita.objects.all()
    for cita in todas_citas:
        if(cita.cliente == cliente):
                citas.append(cita)
    return render(request, 'cuerpo/Citas.html', {'citas': citas,'user':user})

def error(request):
    return  render(request,'cuerpo/404.html')

def packs(request):
    return render(request, 'cuerpo/packs.html')


def promociones(request):
    return render(request, 'cuerpo/promociones.html')


def unete(request):
    return render(request, 'cuerpo/unete.html')


def index(request):
    return  render(request,'cuerpo/index.html')

def acercade(request):
    return  render(request,'cuerpo/acercade.html')

def contacto(request):
    return  render(request,'cuerpo/contacto.html')

def contraseña(request):
    return  render(request,'cuerpo/contraseña.html')


def iniciarSesión(request):
    return  render(request,'cuerpo/iniciarSesión.html')

def unete(request):
    return  render(request,'cuerpo/unete.html')


def agendar_cita(request):
    form = AgendarForm()
    if request.method == 'GET':
        form= AgendarForm(request.GET)
        if form.is_valid():
            #------------------Obtener el usuario actual para asignarselo a la cita
            user = request.session['username']
            cliente = Cliente.objects.get(user=user.lower())
            #----------------------------------------------------------------------
            paquete = form.cleaned_data.get('num_paquete')
            hora_inicio = form.cleaned_data.get('hora_inicio')
            #-------------------Se hacen las validaciones para saber cuanto durará la sesión
            #cita=Cita(cliente=cliente,hora_inicio=hora_inicio,hora_fin=,num_paquete=)
            #------------------------------------------------------Se guarda la cita
            #cita.save()
    return  render(request,'cuerpo/AgendarCita.html',{'form': form})
#--------------------------------------------------------------------------------
def login(request):
    username = None
    form_login= LoginForm()
    if request.method == 'GET':
        if 'action' in request.GET:
            action =request.GET.get('action')
            if action == 'logout':
                if request.session.has_key('username'):
                    request.session.flush()
                #-------------Cuando quiere salir
                return redirect()

        if 'username' in request.session:
            username= request.session['username']
    elif request.method == 'POST':
        form_login= LoginForm(request.POST)
        if form_login.is_valid():
            username= form_login.cleaned_data['username']
            password= form_login.cleaned_data['password']
            #------------------------------------Validaciones login
            try:
                usuario = Cliente.objects.get(user=username)
                if(usuario.password != password):
                    messages.info(request, 'Informacion erronea')
                    #____________________Poner un alert o algo así
                else:
                    messages.info(request, 'Bienvenid@ ' + usuario.user)
                    request.session['username']=username
                    return render(request, 'cuerpo/index.html', {})
            except Cliente.DoesNotExist:
                messages.info(request, 'El usuario no esta registrado')
                username = None
                redirect('login')
    return render(request, 'cuerpo/iniciarSesión.html', {'form': form_login})

def registro(request):
    form=RegistroForm()
    if request.method == 'POST':
        form=RegistroForm(request.POST)
        if form.is_valid():
            #user = form.save(commit=False)
            user= form.cleaned_data.get('user')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            name=form.cleaned_data.get('nombre')
            mail=form.cleaned_data.get('email')
            if(password1 != password2) :
                messages.info(request, 'Contraseñas no concuerdan.')
            else:
                try:
                    Cliente.objects.get(user=user)
                    messages.info(request, 'Usuario ya registrado')
                except Cliente.DoesNotExist:
                    newuser= Cliente(nombre=name,user=user,password=password1,correo=mail)
                    newuser.save()
                    #return redirect('index')


        else:
                messages.info(request, 'Error al llenar los campos')
    return render(request, 'cuerpo/registro.html', {'form': form})

#-----------------------------------------------------------------------------------------
def enviarCorreo(request):
        if request.method == 'POST':
            form = RegistroForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('user')
                mail = form.cleaned_data.get('email')
                user_actual=user
                info_usuario=Cliente.objects.get(user_actual)
                send_mail('Recuperacion de contraseña Infinity Pet',
                        'Tu contraseña es: '+info_usuario.password,
                        'andiee.grr@gmail.com',
                        [info_usuario.correo], fail_silently=False)
        return render(request, 'iniciarSesión.html',{'form':form})