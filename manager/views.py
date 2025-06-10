from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .services.transactions_services import *


# Create your views here.
@permission_classes([IsAuthenticated])
class CreateTransactions(APIView):
    def post(self, request):
        create_result = TransactionsService().create_transaction(request.data)
        return Response(create_result)
