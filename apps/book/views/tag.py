from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.book.models import Tag
from apps.book.serializers import TagSerializer


@api_view()
def list_tags(request):
    # Get all authors using ORM
    tags = Tag.objects.all()

    # Deserialize using  te AuthorSerializer
    data = TagSerializer(tags, many=True)

    # Return data
    return Response(data.data, status=status.HTTP_200_OK)
