from rest_framework import serializers

from account_module.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password']:
            raise serializers.ValidationError('Passwords must match')

        user = User.objects.filter(email=attrs['email']).first()
        if user:
            raise serializers.ValidationError('Email already exists')

        user = User.objects.filter(username=attrs['username']).first()
        if user:
            raise serializers.ValidationError('Username already exists')

        return attrs

    def create(self, validated_data):
        user = User(first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if not user:
            raise serializers.ValidationError('User does not exist')

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError('Invalid password')

        return attrs

