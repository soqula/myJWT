from django.db.models import Q
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile,HistoryWeight


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'username', 'id')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, use_instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                use_instance.set_password(value)
            else:
                setattr(use_instance, attr, value)
        use_instance.save()
        return use_instance


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'user', 'username','opt_disp_list',
        )

class HistoryWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryWeight
        fields = (
            'user', 'saved_at','weight',
        )