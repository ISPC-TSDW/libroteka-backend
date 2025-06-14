import mercadopago

from django.contrib.auth.hashers import check_password
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.conf import settings
from knox.models import AuthToken
from rest_framework import viewsets, generics, permissions, status
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from .serializer import *
from .models import *
from .utils import update_average_rating


@api_view(['POST'])
@permission_classes([AllowAny])
def mercado_pago_webhook(request):
    topic = request.data.get('topic') or request.query_params.get('topic')
    payment_id = request.data.get('data', {}).get('id') or request.data.get('id')

    #procesa pagos
    if topic == 'payment' and payment_id:
        #obtener el estado real del pago
        import mercadopago
        sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN_SANDBOX)
        payment_info = sdk.payment().get(payment_id)
        status_mp = payment_info["response"]["status"]
        preference_id = payment_info["response"]["order"]["id"] if payment_info["response"].get("order") else None

        #busca la orden por preference_id
        if preference_id:
            try:
                order = Order.objects.get(preference_id=preference_id)
                if status_mp == "approved":
                    order.id_Order_Status_id = 2  # Pagada
                elif status_mp == "rejected":
                    order.id_Order_Status_id = 3  # Cancelada
                order.save()
            except Order.DoesNotExist:
                pass  

    return Response({"status": "received"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mercado_pago_preference(request):
    sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN_SANDBOX)
    items = request.data.get('items', [])
    origin = (request.headers.get('Origin') or 'https://5a0e-45-184-104-253.ngrok-free.app' or 'http://localhost:4200').rstrip('/')
    print("Origin:", origin)  
    preference_data = {
        "items": items,
        "payer": {
            "email": request.user.email
        },
        "back_urls": {
            "success": f"{origin}/success",
            "failure": f"{origin}/failure",
            "pending": f"{origin}/pending"
        },
        "auto_return": "approved"
    }
    print("Mercado Pago preference data:", preference_data)  
    preference_response = sdk.preference().create(preference_data)
    if "id" not in preference_response["response"]:
        return Response({
            "error": "No se pudo crear la preferencia de Mercado Pago.",
            "mp_response": preference_response["response"]
        }, status=400)
    preference_id = preference_response["response"]["id"]
    order = Order.objects.create(
        id_User=request.user,
        id_Order_Status=OrderStatus.objects.get(status="Pendiente"),
        books=request.data.get('books', []),
        total=request.data.get('total'),
        books_amount=request.data.get('books_amount'),
        address=request.data.get('address'),
        city=request.data.get('city'),
        telephone=request.data.get('telephone'),
        dni=request.data.get('dni'),
        preference_id=preference_id
    )

    return Response({
        "preference_id": preference_id
    }, status=201)

class IsAdminGroupOrSuperadmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and (
            request.user.is_superuser or request.user.groups.filter(name='Admin').exists()
        )
    

    

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminGroupOrSuperadmin]

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    permission_classes = [IsAdminGroupOrSuperadmin]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminGroupOrSuperadmin]
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminGroupOrSuperadmin]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = [MultiPartParser, FormParser]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UsersLibrotekaViewSet(viewsets.ModelViewSet):
    queryset = UsersLibroteka.objects.all()
    serializer_class = UsersLibrotekaSerializer
    lookup_field = 'email'  


class LibrosView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        books = Book.objects.all()
        books_data = BookSerializer(books, many=True).data
        return Response(books_data, status=status.HTTP_200_OK)
    

class BusquedaLibrosView(APIView):
    permission_classes = [AllowAny] 

    def get(self, request):
        criterio = request.GET.get('criterio')
        value = request.GET.get('value')

        if not criterio or not value:
            return Response({'error': 'Criterio y valor son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        if criterio == 'author':
            books = Book.objects.filter(id_Author__name__icontains=value)
        elif criterio == 'genre':
            books = Book.objects.filter(id_Genre__name__icontains=value)
        elif criterio == 'editorial':
            books = Book.objects.filter(id_Editorial__name__icontains=value)
        elif criterio == 'title':
            books = Book.objects.filter(title__icontains=value)
        else:
            return Response({'error': 'Criterio de búsqueda no válido'}, status=status.HTTP_400_BAD_REQUEST)
        if not books.exists():
            return Response({'message': 'No se encontraron libros que coincidan con la búsqueda'}, status=status.HTTP_200_OK)  
        books_data = BookSerializer(books, many=True).data
        return Response(books_data, status=status.HTTP_200_OK)

class GetBooksByAuthorOrGenreOrTitleView(View):
    def get(self, request, *args, **kwargs):
        criterio = kwargs.get('criterio')
        value = kwargs.get('value')
        if criterio == 'author':
            books = Book.objects.filter(id_Author__name__icontains=value)
        elif criterio == 'genre':
            books = Book.objects.filter(id_Genre__name__icontains=value)
        elif criterio == 'editorial':
            books = Book.objects.filter(id_Editorial__name__icontains=value)
        else:
            return JsonResponse({'error': 'Invalid search criterion'}, status=400)
        data = [{'title': book.title, 
                 'author': book.id_Author.name, 
                 'genre': book.id_Genre.name, 
                 'editorial': book.id_Editorial.name,
                 'description': book.description,
                 'price': book.price,
                 'stock': book.stock} for book in books]
        return JsonResponse(data, safe=False)
   
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Crear el usuario y guardar la contraseña como hash
        user = serializer.save()
        user.password = make_password(user.password)
        user.save()

        # Generar token JWT
        refresh = RefreshToken.for_user(user)
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def perform_create(self, serializer):
        serializer.save(id_User=self.request.user)
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Order.objects.none()
        return Order.objects.filter(id_User=self.request.user).order_by('-date')
    
class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = UsersLibroteka.objects.get(email=email)
                if not user.is_active:
                    return Response({"message": "User account is deactivated"}, status=status.HTTP_403_FORBIDDEN)
                if check_password(password, user.password):
                    # Generar token JWT
                    refresh = RefreshToken.for_user(user)
                    response = Response({
                       'message': 'Inicio de sesión exitoso',
                        'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'role': user.role.id
                    }
                    }, status=status.HTTP_200_OK)                
                # Configuración de cookies HTTP-only para ambos tokens
                    response.set_cookie(
                        key="access_token",
                        value=str(refresh.access_token),
                        httponly=True,
                        secure=True,
                        samesite='Lax'
                    )  
                    response.set_cookie(
                        key="refresh_token",
                        value=str(refresh),
                        httponly=True,
                        secure=True,
                        samesite='Lax'
                    )
                    return response
                else:
                    return Response({"message": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
            except UsersLibroteka.DoesNotExist:
                return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateUserAPI(APIView):
    permission_classes = [IsAuthenticated]
    # TODO: Implementar update con usuario auth
    def put(self, request):
        try:
            user = UsersLibroteka.objects.get(email=request.data.get('email'))
        except UsersLibroteka.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)

        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAdminUser]

class RoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAdminUser]        


class UsersLibrotekaListCreate(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        users = UsersLibroteka.objects.all()
        serializer = UsersLibrotekaSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersLibrotekaSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            cliente_group = Group.objects.get(name="Cliente")
            cliente_group.user_set.add(user)
            return Response({"message": "Usuario registrado con éxito:", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UsersLibrotekaListUser(APIView):
    def get(self, request):
        user_email = request.query_params.get('email', None)

        if user_email:
            user = get_object_or_404(UsersLibroteka, email=user_email)
            serializer = UsersLibrotekaSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
class CreateOrderView(APIView):
    def post(self, request):
        user_email = request.data.get('id_User')
        try:
            user = UsersLibroteka.objects.get(email=user_email)
        except UsersLibroteka.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        order_status_str = request.data.get('id_Order_Status')
        try:
            order_status = OrderStatus.objects.get(status=order_status_str)
        except OrderStatus.DoesNotExist:
            # logger.error(f"Order status {order_status_str} does not exist.")
            return Response({"message": "Order status does not exist"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'id_Order_Status': order_status.id_Order_Status,
            'id_User': user.email,
            'date': request.data.get('date'),
            'books': request.data.get('books'),
            'total': request.data.get('total'),
            'books_amount': request.data.get('books_amount')
        }

        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # logger.error(f"Serializer errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FavoriteManageView(APIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def post(self, request):
        user_id = request.data.get('id_user')
        book_id = request.data.get('id_book')

        if Favorite.objects.filter(id_user=user_id, id_book=book_id).exists():
            return Response({"detail": "Book is already in your favorites."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_data['message']= 'The book was added to favorites.'
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_id = request.query_params.get('id_user', None)

        if user_id:
            favorites = Favorite.objects.filter(id_user=user_id)
        else:
            favorites = Favorite.objects.all()

        serializer = self.serializer_class(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteFavoriteView(APIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


    def delete(self, request, pk):
        favorite = Favorite.objects.filter(pk=pk).first()

        if favorite:
            favorite.delete()
            return Response({'message': 'Removed from favorites'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'message': 'Not in favorites'}, status=status.HTTP_404_NOT_FOUND)

class RatingManageView(APIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    @transaction.atomic
    def post(self,request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid():
            rating = serializer.save()
            update_average_rating(rating.id_book.id_Book)
            response_data = serializer.data
            response_data['message']= 'Your rating was sent.'
            return Response(response_data, status=status.HTTP_201_CREATED)

        response_error = serializer.errors
        response_error['message'] =  'There was an issue with your request.'
        return Response(response_error, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_id = request.query_params.get('id_user', None)

        if user_id:
            rating = Rating.objects.filter(id_user=user_id)
        else:
            rating = Rating.objects.all()

        serializer = self.serializer_class(rating, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ModifyRatingView(APIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    @transaction.atomic
    def put(self, request, pk):
        rating = get_object_or_404(self.queryset, pk=pk)
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            update_average_rating(rating.id_book.id_Book)
            response_data = serializer.data
            response_data['message']= 'Your rating has been updated.'
            return Response(response_data, status=status.HTTP_200_OK)

        response_error = serializer.errors
        response_error['message'] =  'There was an issue with your request.'
        return Response(response_error, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, pk):
        rating = get_object_or_404(Rating, pk=pk)
        book_id = rating.id_book.id_Book
        rating.delete()
        update_average_rating(book_id)

        return Response({'message': 'Rating removed.'}, status=status.HTTP_204_NO_CONTENT)




    def get(self, request):
        user_id = request.query_params.get('id_user', None)

        if user_id:
            user = UserLibrotekaSerializer.objects.filter(id_user=user_id)
        else:
            favorites = Favorite.objects.all()

        serializer = self.serializer_class(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class MeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role.id if hasattr(user, 'role') else None,
        })