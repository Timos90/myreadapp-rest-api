from rest_framework import serializers
from apps.book.models import Author

class AuthorSerializer(serializers.ModelSerializer):

    name = serializers.CharField(read_only=True)
    username = serializers.SerializerMethodField()

    def get_username(self, obj): # get serializer method field
        return '_'.join([obj.first_name, obj.last_name])

    def validate_first_name(self, value):  # validate_<field-name>
        """ field level validation """
        if '-' in value:  #(-) = hyphen
            raise serializers.ValidationError('first name should not contain hyphen (-)')
        return value

    def validate(self, attrs): # validate
        """ Object level validation """
        if attrs.get('first_name') == attrs.get('last_name'):
            raise serializers.ValidationError('first name and last name should not be the same')

        return attrs

    

    class Meta:
        model = Author
        fields = '__all__'   # ('id', 'first_name', 'last_name')
        read_only_fields = ('id', )
