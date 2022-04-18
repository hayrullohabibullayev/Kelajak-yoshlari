from django.shortcuts import redirect, render
from .models import *
from .froms import *
from django.db.models import FloatField
from django.db.models import F
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

################################### login or register #################################

def loginUsers(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username or password was incorrect")
    context = {
    }            
    return render(request, 'siteapp/log_register/login.html')

def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')
    context = {
        'form':form
    }    
    return render(request, 'siteapp/log_register/register.html', context)

def dashboard(request):
    sardorlar = KamalakSardorlarLoyihasi.objects.all()
    sardor = IttifoqSardorlarLoyihasi.objects.all()
    context = {
        'sardorlar':sardorlar,
        'sardor':sardor,
    }
    return render(request, 'siteapp/index.html', context)

def dashboard3(request):
    murojaat_soni = Comment.objects.all().count()
    murojaat = Comment.objects.all()
    context = {
        'murojaat_soni':murojaat_soni,
        'murojaat':murojaat,
    }
    return render(request, 'siteapp/index3.html', context)

def dashboard2(request):
    book = Create_book.objects.all()
    qiziq = Platformaga_qiziqishlar.objects.all()
    income1 = Platformaga_qiziqishlar.objects.all().count()
    income2 = Platformaga_qiziqishlar.objects.all().count()
    income = Create_book.objects.all().count()
    context = {
        'book':book,
        'income':income,
        'income1':income1,
        'income2':income2
    }
    return render(request, 'siteapp/index2.html', context)

def abaut(request):
    return render(request, 'siteapp/html/about.html')

def musobaqa(request):
    return render(request, 'siteapp/html/musobaqa.html')

def batafsil(request):
    return render(request, 'siteapp/html/blog-single.html')

def aloqa(request):
    return render(request, 'siteapp/aloqa.html')

def comment(request):
    form = CreateCommitForm()
    if request.method == 'POST':
        form = CreateCommitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coms')
        else:
            form = CreateCommitForm()
    context = {
        'form':form
    }
    return render(request, 'siteapp/comment.html', context)

def savol_javob_sahifasi(request):
    return render(request, 'siteapp/html/savol.html')

def savollar(request):
    savol = Savollar.objects.all()
    context = {
        'savol':savol
    }
    return render(request, 'siteapp/html/savollar.html', context)

def javob(request):
    form = Createsavollarga_javobForm()
    if request.method == 'POST':
        form = Createsavollarga_javobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('javob')
        else:
            form = Createsavollarga_javobForm()
    context = {
        'form':form
    }
    return render(request, 'siteapp/html/javob.html', context)

def masofaviy_oquv_kursi(request):
    return render(request, 'siteapp/fanlar/index.html')

def dasturlash(request):
    return render(request, 'siteapp/fanlar/contact.html')

def tarix(request):
    return render(request, 'siteapp/fanlar/tarix.html')

def matematika(request):
    return render(request, 'siteapp/fanlar/matematika.html')

def reytinglar(request):
    return render(request, 'siteapp/html/reyting.html')

def chat(request):
    chat_message = Chatmessage.objects.all()
    form = ChatmessageForm()
    if request.method == 'POST':
        form = ChatmessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
        else:
            form = ChatmessageForm()
    context = {
        'form':form,
        'chat_message':chat_message
    }
    return render(request, 'siteapp/chat.html', context)