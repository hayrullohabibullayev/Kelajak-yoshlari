from django.db import models

# Create your models here.

class Create_book(models.Model):
    avatar = models.ImageField(upload_to='profile', blank=True, null=True)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text
    
class Platformaga_qiziqishlar(models.Model):
    QIZIQISH_CHOISEC = [
        ('yaxshi', 'yaxshi'),
        ("zo'r", "zo'r")
    ]
    qiziqish = models.CharField(max_length=9, choices=QIZIQISH_CHOISEC, default='Yaxshi') # Darajasi
    coment = models.TextField()
    
class KamalakSardorlarLoyihasi(models.Model):
    avatar = models.ImageField(upload_to='kamalak', blank=True, null=True)
    project_name = models.CharField(max_length=2500)
    
    def __str__(self):
        return self.project_name
    
class IttifoqSardorlarLoyihasi(models.Model):    
    avatar = models.ImageField(upload_to='Itifoq', blank=True, null=True)
    project_name = models.CharField(max_length=2500)
    
    def __str__(self):
        return self.project_name
    
class Sardorlarhaqida(models.Model):
    avatar = models.ImageField(upload_to='kamalak', blank=True, null=True)
    full_name = models.CharField(max_length=2500)
    yunalishi = models.CharField(max_length=2550)
    
    def __str__(self):
        return self.full_name
    
class Comment(models.Model):
    murojaat = models.CharField(max_length=50000)
    telefon_raqam = models.CharField(max_length=50000)
    
    def __str__(self):
        return self.murojaat

class Savollar(models.Model):
    savolni_soni = models.CharField(max_length=500)
    savol = models.CharField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.savolni_soni
    
class Savollarga_javob_yozish(models.Model):
    savolni_sonini_belgilash = models.ForeignKey(Savollar,  on_delete=models.CASCADE)
    savolga_javobni_yozish = models.CharField(max_length=5000)
    telfon_raqam = models.CharField(max_length=20)
    
    def __str__(self):
        return self.savolga_javobni_yozish
   
class Chatmessage(models.Model):
    message = models.CharField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message    
    
        
