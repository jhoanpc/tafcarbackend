from django.db import models
from utils.model_abstracts import Model
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Person(Model):
    class TypeDoc(models.TextChoices):
        NIT = "Nit"
        CC  = "CC"
    
    class GenereType(models.TextChoices):
        MALE = "Masculino"
        FEMI = "Femenino"
    fullname  = models.CharField(max_length=100, null=False)
    created_at  = models.DateTimeField(auto_now=True)
    typedoc     = models.CharField(max_length=4, choices=TypeDoc.choices, null=False)
    nroDoc         = models.CharField(max_length=14,null=False )
    gender      = models.CharField(max_length=10, null=False, choices=GenereType.choices)
    
    @property
    def fullName(self):
        return f"{self.fullname}"
    class Meta:
        verbose_name_plural='people'
    
    def __str__(self):
        return self.fullName

class DetailsPerson(Model):
    class HomeType(models.TextChoices):
        PROPIA = "Propia"
        FAMILIAR = "Familiar"
        ARRIENDO = "Arriendo"
    person          = models.ForeignKey(Person,related_name='detailspersons',on_delete=models.CASCADE)
    dateexpnrodoc   = models.DateTimeField(null=False)
    cityexpnrodoc   = models.CharField(max_length=25, null=False)
    birthcity       = models.CharField(max_length=50, null=False)
    birthdate       = models.DateField(null=False)
    streetaddress   = models.TextField(max_length=255)
    neighborhood    = models.CharField(max_length=50, null=True)
    hometype        = models.CharField(max_length=15, choices=HomeType.choices, null=False)
    phonenumber     = models.CharField(max_length=14, null=False)
    phonenum        = models.CharField(max_length=14, null=False)
    cityresidence   = models.CharField(max_length=100, null=False, verbose_name="Ciudad Residencia")
    email           = models.EmailField(verbose_name="Email", null=True)
    familiarref     = models.CharField(max_length=50, null=True)
    familiaper      = models.CharField(max_length=50, null=True)
    famirefphone    = models.CharField(max_length=14, null=True)
    refperphone     = models.CharField(max_length=14, null=True)
    
    
    
    class Meta:
        verbose_name_plural= 'DetailsPeople'
        
    def __str__(self):
        return self.email
    

class DetailsEconomicActivity(Model):
    class TypeActivity(models.TextChoices):
        EMPLOYEE    = "Empleado"
        INDEPENDENT = "Independiente"
        RENTCAPI    = "Rentista de Capital"
        PENSION     = "Pensionado"
    person              = models.ForeignKey(Person,related_name='detailseconomicactivitys',on_delete=models.CASCADE)
    typeactivity        = models.CharField(max_length=25, choices=TypeActivity.choices,null=False)
    bussinesname        = models.CharField(max_length=50, null=True)
    bussinessaddres     = models.CharField(max_length=100, null=True)
    bussinessphone      = models.CharField(max_length=14, null=True)
    jobposition         = models.CharField(max_length=25, null=True)
    startdatejob        = models.DateTimeField(null=True)
    contrattype         = models.CharField(max_length=25)
    timejobpos          = models.IntegerField(null=True)
    pensionfund         = models.CharField(max_length=50, null=True)
    startDatePF         = models.DateTimeField(null=True)
    rut                 = models.CharField(max_length=14, null=True)
    timeactivityrut     = models.IntegerField(null=True)
    bussinesnameind1    = models.CharField(max_length=50, null=True)
    nitind1             = models.CharField(max_length=14, null=True)
    phoneind1           = models.CharField(max_length=14, null=True)
    bussinesnameind2    = models.CharField(max_length=50, null=True)
    nitind2             = models.CharField(max_length=14, null=True)
    phoneind2           = models.CharField(max_length=14, null=True)
    bussinesnameind3    = models.CharField(max_length=50, null=True)
    nitind3             = models.CharField(max_length=14, null=True)
    phoneind3           = models.CharField(max_length=14, null=True)
    totalincome     = models.DecimalField(max_digits=10,decimal_places=2)
    rentdel         = models.BooleanField(default=False, null=True)
    totalexpenses   = models.DecimalField(max_digits=10,decimal_places=2)
    totalassets     = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        verbose_name_plural: "DetailsEconomicActivity"
    def __str__(self):
        return self.bussinesname    
    
    