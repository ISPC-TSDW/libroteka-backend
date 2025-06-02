from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id_Author', 'name']

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ['id_Editorial', 'name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id_Genre', 'name']

class BookSerializer(serializers.ModelSerializer):
    id_Author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), allow_null=True)
    id_Genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)
    id_Editorial = serializers.PrimaryKeyRelatedField(queryset=Editorial.objects.all(), allow_null=True)
    avg_rating = serializers.FloatField(read_only=True)
    #image = serializers.ImageField(use_url=True, required=False)
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
         return obj.image.url if obj.image else None

    class Meta:
        model = Book
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'dni']
class UserLibrotekaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'dni', 'email', 'password', 'is_active'] 

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)        

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersLibroteka
        fields = ('id', 'username', 'email', 'password', 'dni')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UsersLibroteka.objects.create_user(
            username=validated_data['username'], 
            email=validated_data['email'], 
            password=validated_data['password'],
            dni=validated_data.get('dni') 
        )
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Role
        fields = ['id', 'name', 'description']     



class UsersLibrotekaSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UsersLibroteka
        fields = ['id', 'username', 'first_name', 'last_name', 'dni', 'email', 'password', 'is_active']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
    
class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    dni = serializers.CharField(required=False)
    password = serializers.CharField(required=False, write_only=True)
    is_active = serializers.BooleanField(required=False)
    class Meta:
        model = UsersLibroteka
        fields = ['username', 'first_name', 'last_name', 'dni', 'email', 'password',  'is_active']
        extra_kwargs = {
            'email': {'read_only': True}, 
            'password': {'write_only': True},
        }
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id_Order', 'date', 'id_User']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    def validate(self, data):

        if not data['id_user'].is_active:
            raise serializers.ValidationError({"detail": "User account is deactivated."})
        return data

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

    def validate(self, data):

        if not data['id_user'].is_active:
            raise serializers.ValidationError({"detail": "User account is deactivated."})
        return data

