from rest_framework import serializers
from apps.book.models import Tag
import re

class TagSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name.capitalize()

    def validate_special_characters(self, value):  # validate_<field-name>
        """ field level validation """
        if re.search(r'[!@#$%^&*]', value):
            raise serializers.ValidationError("Tag name should not contain special characters like !@#$%^&*")
        return value


    class Meta:
        model = Tag
        fields = '__all__'
        # exclude = ('one of them', )
        read_only_fields = ('id', )
