from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .services.transactions_services import *


# Create your views here.
@permission_classes([IsAuthenticated])
class CreateTransactions(APIView):
    def post(self, request):
        data = request.data

        create_result = TransactionsService().create_transaction(data)
        return Response(create_result)


@permission_classes([IsAuthenticated])
class DeleteTransaction(APIView):
    def post(self, request):
        data = request.data

        delete_result = TransactionsService().delete_transaction(data)
        return Response(delete_result)


@permission_classes([IsAuthenticated])
class EditTransaction(APIView):
    def post(self, request):
        data = request.data

        edit_result = TransactionsService().edit_transaction(data)
        return Response(edit_result)