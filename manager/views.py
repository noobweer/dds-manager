from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .services.transactions_services import *
from .services.statuses_service import *
from .services.types_service import *
from .services.categories_service import *
from .services.subcategories_service import *


# Create your views here.
@permission_classes([IsAuthenticated])
class CreateTransactionView(APIView):
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
class TransactionsView(APIView):
    def post(self, request):
        data = request.data

        transactions_result = TransactionsService().all_transactions(data)
        return Response(transactions_result)


@permission_classes([IsAuthenticated])
class CreateStatusView(APIView):
    def post(self, request):
        data = request.data

        create_result = StatusesService().create_status(data)
        return Response(create_result)


@permission_classes([IsAuthenticated])
class EditStatusView(APIView):
    def post(self, request):
        data = request.data

        edit_result = StatusesService().edit_status(data)
        return Response(edit_result)


@permission_classes([IsAuthenticated])
class DeleteStatusView(APIView):
    def post(self, request):
        data = request.data

        delete_result = StatusesService().delete_status(data)
        return Response(delete_result)


@permission_classes([IsAuthenticated])
class StatusesView(APIView):
    def get(self, request):
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
    def get(self, request):
        types_result = OperationTypeService().all_types()
        return Response(types_result)


@permission_classes([IsAuthenticated])
class CreateCategoryView(APIView):
    def post(self, request):
        data = request.data

        create_result = CategoryService().create_category(data)
        return Response(create_result)


@permission_classes([IsAuthenticated])
class EditCategoryView(APIView):
    def post(self, request):
        data = request.data

        edit_result = CategoryService().edit_category(data)
        return Response(edit_result)


@permission_classes([IsAuthenticated])
class DeleteCategoryView(APIView):
    def post(self, request):
        data = request.data

        delete_result = CategoryService().delete_category(data)
        return Response(delete_result)


@permission_classes([IsAuthenticated])
class CategoriesView(APIView):
    def get(self, request):
        categories_result = CategoryService().all_categories()
        return Response(categories_result)


@permission_classes([IsAuthenticated])
class CreateSubcategoryView(APIView):
    def post(self, request):
        data = request.data

        create_result = SubcategoryService().create_subcategory(data)
        return Response(create_result)


@permission_classes([IsAuthenticated])
class EditSubcategoryView(APIView):
    def post(self, request):
        data = request.data

        edit_result = SubcategoryService().edit_subcategory(data)
        return Response(edit_result)


@permission_classes([IsAuthenticated])
class DeleteSubcategoryView(APIView):
    def post(self, request):
        data = request.data

        delete_result = SubcategoryService().delete_subcategory(data)
        return Response(delete_result)


@permission_classes([IsAuthenticated])
class SubcategoriesView(APIView):
    def get(self, request):
        subcategories_result = SubcategoryService().all_subcategories()
        return Response(subcategories_result)