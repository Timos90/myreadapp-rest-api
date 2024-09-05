# TODO: Create a custom permission that will make sure that
# it checks the authentication user id is the same as the reader user

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# IsAuthenticated -> If user is not authenticated, it will fail
# IsAdminUser -> If 'is_staff' is 'False', it will fail
# IsAuthenticatedOrReadOnly -> CRUD
    # POST
    # GET -> READ ONLY, DOESNT NEED AUTHENTICATION
    # PUT/PATCH
    # DELETE
