from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'is_active']
             
class CreateKamalakSardorlarLoyihasiForm(forms.ModelForm):
    class Meta:
        model = KamalakSardorlarLoyihasi
        fields = "__all__"


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Create_book
        fields = "__all__"

class CreateIttifoqSardorlarLoyihasiForm(forms.ModelForm):
    class Meta:
        model = IttifoqSardorlarLoyihasi
        fields = "__all__"

class CreateCommitForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        
class Createsavollarga_javobForm(forms.ModelForm):
    class Meta:
        model = Savollarga_javob_yozish
        fields = "__all__"
        
class ChatmessageForm(forms.ModelForm):
    class Meta:
        model = Chatmessage
        fields = ['message']