from ..models import Cup

from rest_framework import serializers

# Serializers define the API representation.


class CupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cup
        fields = ('id', 'title', 'description', 'created_by')
