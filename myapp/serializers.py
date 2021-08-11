from rest_framework import serializers
from .models import Restorent

class RestorentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restorent
		fields = '__all__'
