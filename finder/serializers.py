from rest_framework import serializers

from .models import Museum


class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = ['name', 'category', 'city', 'description', 'website']
        
class MuseumAdminAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = ['id','name', 'category', 'city', 'description', 'website']
        
        
        
        
        
        
        
        
        
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('password', 'user_permissions', 'is_authenticated')