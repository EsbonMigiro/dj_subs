from rest_framework import serializers
from serializer_app.models import SerializerModel

class ModelSerializerr(serializers.ModelSerializer):
      class Meta:
        model = SerializerModel
        fields = ['email', 'password']
