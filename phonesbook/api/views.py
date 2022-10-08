from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from contacts.models import Contact
from .serializers import ContactSerializer


class GetContactsAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request: Request, *args, **kwargs) -> Response:
        user = request.user
        contacts = Contact.objects.filter(owner=user)

        return Response(
            ContactSerializer(contacts, many=True).data
        )

