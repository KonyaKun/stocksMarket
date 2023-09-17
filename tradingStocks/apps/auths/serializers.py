from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    EmailField,
    BooleanField,
    DateTimeField,
    CharField,
    ImageField,
    DecimalField,
)
from auths.models import CustomUser

# For converting QuerySet to JSON files

class CustomUserSerializer(ModelSerializer):
    """CustomUserSerializer."""
    id = IntegerField(read_only=True)
    user_name = CharField(required=True)
    first_name = CharField(required=True)
    last_name = CharField(required=True)
    email = EmailField(required=True)
    image_url = ImageField(allow_empty_file=True, required=False)
    password = CharField(required=True)
    is_active = BooleanField(read_only=True)
    is_staff = BooleanField(read_only=True)
    date_joined = DateTimeField(read_only=True)
    datetime_created = DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S")
    datetime_updated = DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S")
    datetime_deleted = DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S")

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'user_name',
            'first_name',
            'last_name',
            'email',
            'image_url',
            'password',
            'is_active',
            'is_staff',
            'date_joined',
            'datetime_created',
            'datetime_updated',
            'datetime_deleted'
        ]
        
    def create(self, validated_data):
        user = CustomUser.objects.create(
            user_name=validated_data['user_name'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            image_url=validated_data['image_url'],
            email=validated_data['email'],
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    
