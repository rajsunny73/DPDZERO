from rest_framework import serializers
from DPZERO.models import RegisterModels,TokenModels,StorageModels
class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegisterModels
        fields = '__all__'
    
class TokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = TokenModels
        fields = '__all__'

class StorageSerializers(serializers.ModelSerializer):
    class Meta:
        model = StorageModels
        fields = '__all__'   

  