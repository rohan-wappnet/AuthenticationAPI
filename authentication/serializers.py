from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

MIN_LENGTH = 2


class RegSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters"
        }
    )

    password2 = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters"
        }
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'password2', 'email']

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password does not match")
        return data

    def create(self, validated_data):
        # User.objects.create(**validated_data)
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class GetLoginTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password', 'email']