from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .services.transactions_services import *
from .services.statuses_service import *
from .services.types_service import *


# Create your views here.
@permission_classes([IsAuthenticated])
class CreateTransactionsView(APIView):
    def post(self, request):
        data = request.data

        create_result = TransactionsService().create_transaction(data)
        return Response(create_result)


@permission_classes([IsAuthenticated])
class DeleteTransactionView(APIView):
    def post(self, request):
        data = request.data

        delete_result = TransactionsService().delete_transaction(data)
        return Response(delete_result)


@permission_classes([IsAuthenticated])
class EditTransactionView(APIView):
    def post(self, request):
        data = request.data

        edit_result = TransactionsService().edit_transaction(data)
        return Response(edit_result)


@permission_classes([IsAuthenticated])
class StatusCreateView(APIView):
    def post(self, request):
        data = request.data

        create_result = StatusesService().create_status(data)
        return Response(create_result)


@permission_classes([IsAuthenticated])
class StatusEditView(APIView):
    def post(self, request):
        data = request.data

        edit_result = StatusesService().edit_status(data)
        return Response(edit_result)


@permission_classes([IsAuthenticated])
class StatusDeleteView(APIView):
    def post(self, request):
        data = request.data

        delete_result = StatusesService().delete_status(data)
        return Response(delete_result)


@permission_classes([IsAuthenticated])
class StatusesView(APIView):
    def get(self):
        statuses_result = StatusesService().all_statuses()
        return Response(statuses_result)


@permission_classes([IsAuthenticated])
class CreateTypeView(APIView):
    def post(self, request):
        data = request.data

        create_result = OperationTypeService().create_type(data)
        return Response(create_result)


@permission_classes([IsAuthenticated])
class EditTypeView(APIView):
    def post(self, request):
        data = request.data

        edit_result = OperationTypeService().edit_type(data)
        return Response(edit_result)


@permission_classes([IsAuthenticated])
class DeleteTypeView(APIView):
    def post(self, request):
        data = request.data

        delete_result = OperationTypeService().delete_type(data)
        return Response(delete_result)


@permission_classes([IsAuthenticated])
class TypesView(APIView):
    def get(self):
        types_result = OperationTypeService().all_types()
        return Response(types_result)


