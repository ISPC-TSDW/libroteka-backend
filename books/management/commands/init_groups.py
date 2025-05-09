from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from books.models import Book, Rating, Favorite, Order

class Command(BaseCommand):
    help = 'Crear grupos de usuarios: administrador y cliente'

    def handle(self, *args, **kwargs):
        # Grupo: administrador
        admin_group, _ = Group.objects.get_or_create(name='administrador')
        admin_perms = Permission.objects.filter(
            content_type__model__in=['book', 'author', 'editorial', 'genre', 'order']
        )
        admin_group.permissions.set(admin_perms)
        self.stdout.write(self.style.SUCCESS("Grupo 'administrador' creado."))

        # Grupo: cliente
        client_group, _ = Group.objects.get_or_create(name='clientes')
        client_perms = Permission.objects.filter(
            content_type__model__in=['book', 'rating', 'favorite', 'order'],
            codename__in=[
                # Ratings
                'add_rating', 'change_rating', 'delete_rating', 'view_rating',
                # Favorites
                'add_favorite', 'delete_favorite', 'view_favorite',
                # Orders
                'add_order', 'change_order', 'delete_order', 'view_order',
                # Books (solo ver)
                'view_book'
            ]
        )
        client_group.permissions.set(client_perms)
        self.stdout.write(self.style.SUCCESS("Grupo 'clientes' creado."))
