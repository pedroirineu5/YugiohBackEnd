from rest_framework import serializers

from packs.models import Pack


class PackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = "__all__"
