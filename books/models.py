from django.db import models
from isbn_field import ISBNField
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from datetime import datetime
from cloudinary.models import CloudinaryField




class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()    

class Author(models.Model):

    id_Author = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    country= models.CharField(max_length=50)

    class Meta:
        db_table= 'author'
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
    
class Editorial(models.Model):

    id_Editorial = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    
    class Meta:
        db_table= 'editorial'
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
    
class Genre(models.Model):

    id_Genre = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    
    class Meta:
        db_table= 'genre'
        verbose_name = "Género"
        verbose_name_plural = "Géneros"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
    
current_year = datetime.now().year

isbn_validator = RegexValidator(
    regex=r'^\d{10}(\d{3})?$',
    message='El ISBN debe tener 10 o 13 dígitos numéricos.'
)

        
class Book(models.Model):

    id_Book = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    id_Author = models.ForeignKey(Author, to_field='id_Author', on_delete=models.CASCADE, blank=True, null=True)
    id_Genre = models.ForeignKey(Genre, to_field='id_Genre', on_delete=models.CASCADE, blank=True, null=True)
    description= models.TextField(max_length=1500)
    price= models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    stock= models.PositiveIntegerField(default=1000)
    id_Editorial = models.ForeignKey(Editorial, to_field='id_Editorial', on_delete=models.CASCADE, blank=True, null=True)
    avg_rating = models.FloatField(default=0.0, blank=True)
    ISBN = models.CharField(
        max_length=13,
        validators=[isbn_validator],
        blank=True)
    year = models.PositiveSmallIntegerField(
        default=2000,
        validators=[
            MinValueValidator(1000), 
            MaxValueValidator(current_year)
        ]
    )
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        db_table= 'book'
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
        
    
class OrderStatus(models.Model):
    class Status(models.TextChoices):
        PENDING = ('Pendiente')
        PAID = ('Pagado')
        CANCELED = ('Cancelado')
        PREPARING = ('En preparación')
        SENT = ('Enviado')
        RECEIVED = ('Recibido')

    id_Order_Status = models.AutoField(primary_key=True)
    status = models.CharField(
        choices=Status.choices,
        default=Status.PENDING,
        max_length=15
    )

    class Meta:
        db_table= 'OrderStatus'
        verbose_name = "Estado de la orden"
        verbose_name_plural = "Estados de las órdenes"

    def __unicode__(self):
        return self.status

    def __str__(self):
        return self.status



class UsersLibroteka(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(2)])
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=35 , validators=[MinLengthValidator(2)])
    dni = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(blank=False, default=True)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL, default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'dni','is_active']


    
    class Meta:
        db_table= 'users_libroteka'
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
    
class Order(models.Model):

    id_Order = models.AutoField(primary_key=True)
    id_Order_Status = models.ForeignKey(OrderStatus, to_field='id_Order_Status', on_delete=models.CASCADE)   
    id_User = models.ForeignKey(UsersLibroteka, to_field='email', null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    books = models.JSONField(default=list)
    total = models.DecimalField(blank=False, decimal_places=2, max_digits=10)
    books_amount = models.IntegerField(blank=False)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True)
    preference_id = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table= 'Orders'
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"

    def __unicode__(self):
        return self.id_Order

    def __str__(self):
        return self.id_Order

class Favorite(models.Model):
    id_user = models.ForeignKey(UsersLibroteka, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_user', 'id_book')
        db_table = 'Favorite'
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

    def __str__(self):
        return f"{self.id_user} - {self.id_book.title}"

class Rating(models.Model):
    id_user = models.ForeignKey(UsersLibroteka, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('id_user', 'id_book')
        db_table = 'Rating'
        verbose_name = 'Valoracion'
        verbose_name_plural = 'Valoraciones'

    def __str__(self):
        return f"{self.id_user} - {self.id_book.title} - {self.rating} estrellas"
