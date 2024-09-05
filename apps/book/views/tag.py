from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.book.models import Tag
from apps.book.serializers import TagSerializer


""" 
curl http://127.0.0.1:8000/api/v1/book/tag/
token_header = 'Authorization: Token bb1bf9a858e4cd17a718f97cb4fb4ec0e821e621

curl -H 'Authorization: Token bb1bf9a858e4cd17a718f97cb4fb4ec0e821e621' http://127.0.0.1:8000/api/v1/book/tag/
"""

@api_view()
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_tags(request):
    # Get all authors using ORM
    tags = Tag.objects.all()

    # Deserialize using  te AuthorSerializer
    data = TagSerializer(tags, many=True)

    # Return data
    return Response(data.data, status=status.HTTP_200_OK)
