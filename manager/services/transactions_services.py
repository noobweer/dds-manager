from datetime import datetime

from ..models import *
from ..serializers import *


class TransactionsService:
    def __init__(self):
        self.Transaction = Transaction.objects
        self.Status = Status.objects
        self.OperationType = OperationType.objects
        self.Category = Category.objects
        self.Subcategory = Subcategory.objects

    # TransactionsView with filters (date, status, type, category, subcategory)
    def all_transactions(self, data):
        try:
            status_list = data.get('status', [])
            type_list = data.get('type', [])
            category_list = data.get('category', [])
            subcategory_list = data.get('subcategory', [])
            date_list = data.get('date', [])

            result = self.Transaction.all()

            if date_list:
                if len(date_list) == 2:
                    date_from_str, date_to_str = date_list
                    if date_to_str == '1970-01-01':
                        # Одна дата
                        try:
                            single_date = datetime.strptime(date_from_str, '%Y-%m-%d').date()
                            result = result.filter(created_date=single_date)
                        except ValueError:
                            return {'success': False, 'transactions': []}
                    else:
                        # Диапазон дат
                        try:
                            date_from = datetime.strptime(date_from_str, '%Y-%m-%d').date()
                            date_to = datetime.strptime(date_to_str, '%Y-%m-%d').date()

                            if date_from > date_to:
                                return {'success': False, 'transactions': []}

                            result = result.filter(
                                created_date__gte=date_from,
                                created_date__lte=date_to
                            )
                        except ValueError:
                            return {'success': False, 'transactions': []}
                else:
                    return {'success': False, 'transactions': []}

            if status_list:
                valid_statuses = []
                for status_name in status_list:
                    if not self.Status.filter(name=status_name).exists():
                        return {'success': False, 'transactions': []}
                    valid_statuses.append(self.Status.get(name=status_name))

                result = result.filter(status__in=valid_statuses)

            if type_list:
                valid_types = []
                for type_name in type_list:
                    if not self.OperationType.filter(name=type_name).exists():
                        return {'success': False, 'transactions': []}
                    valid_types.append(self.OperationType.get(name=type_name))

                result = result.filter(type__in=valid_types)

            if category_list:
                valid_categories = []
                for category_name in category_list:
                    if not self.Category.filter(name=category_name).exists():
                        return {'success': False, 'transactions': []}
                    valid_categories.append(self.Category.get(name=category_name))

                result = result.filter(category__in=valid_categories)

            if subcategory_list:
                valid_subcategories = []
                for subcategory_name in subcategory_list:
                    if not self.Subcategory.filter(name=subcategory_name).exists():
                        return {'success': False, 'transactions': []}
                    valid_subcategories.append(self.Subcategory.get(name=subcategory_name))

                result = result.filter(subcategory__in=valid_subcategories)

            serializer = TransactionSerializer(result, many=True)
            return {'success': True, 'transactions': serializer.data}
        except Exception as e:
            print(e)
            return {'success': False, 'transactions': []}

    def create_transaction(self, data):
        try:
            status_name = data.get('status')
            operation_type = data.get('operation_type')
            category_name = data.get('category')
            subcategory_name = data.get('subcategory')
            amount = data.get('amount')
            comment = data.get('comment')

            if not all([status_name, operation_type, category_name, subcategory_name, amount]):
                return {'is_created': False,
                        'message': 'Send all required fields (status, operation_type, category, subcategory, amount)'}

            if not self.Status.filter(name=status_name).exists():
                return {'is_created': False, 'message': f'Invalid status: {status_name}'}
            status_obj = self.Status.get(name=status_name)

            if not self.OperationType.filter(name=operation_type).exists():
                return {'is_created': False, 'message': f'Invalid operation_type: {operation_type}'}
            operation_obj = self.OperationType.get(name=operation_type)

            if not self.Category.filter(name=category_name, type=operation_obj).exists():
                return {'is_created': False, 'message': f'Invalid category: {category_name}'}
            category_obj = self.Category.get(name=category_name, type=operation_obj)

            if not self.Subcategory.filter(name=subcategory_name, category=category_obj).exists():
                return {'is_created': False, 'message': f'Invalid subcategory: {subcategory_name}'}
            subcategory_obj = self.Subcategory.get(name=subcategory_name, category=category_obj)

            self.Transaction.create(status=status_obj, type=operation_obj, category=category_obj,
                                    subcategory=subcategory_obj, amount=amount, comment=comment)
            return {'is_created': True, 'message': f'Transaction created successfully'}
        except Exception as e:
            return {'is_created': False, 'message': str(e)}

    def delete_transaction(self, data):
        try:
            transaction_id = data.get('transaction_id')

            if not self.Transaction.filter(id=transaction_id).exists():
                return {'is_deleted': False, 'message': f'Invalid transaction_id ({transaction_id})'}

            self.Transaction.filter(id=transaction_id).delete()

            return {'is_deleted': True, 'message': f'Transaction deleted successfully'}
        except Exception as e:
            return {'is_deleted': False, 'message': str(e)}

    def edit_transaction(self, data):
        try:
            transaction_id = data.get('transaction_id')
            status_name = data.get('status')
            operation_type = data.get('operation_type')
            category_name = data.get('category')
            subcategory_name = data.get('subcategory')
            amount = data.get('amount')
            comment = data.get('comment')

            if not all([transaction_id, status_name, operation_type, category_name, subcategory_name, amount]):
                return {'is_edited': False,
                        'message': 'Send all required fields (transaction_id, status, operation_type, category, subcategory, amount)'}

            if not self.Transaction.filter(id=transaction_id).exists():
                return {'is_edited': False, 'message': f'Invalid transaction_id ({transaction_id})'}
            transaction_obj = self.Transaction.get(id=transaction_id)

            if not self.Status.filter(name=status_name).exists():
                return {'is_edited': False, 'message': f'Invalid status: {status_name}'}
            status_obj = self.Status.get(name=status_name)

            if not self.OperationType.filter(name=operation_type).exists():
                return {'is_edited': False, 'message': f'Invalid operation_type: {operation_type}'}
            operation_obj = self.OperationType.get(name=operation_type)

            if not self.Category.filter(name=category_name, type=operation_obj).exists():
                return {'is_edited': False, 'message': f'Invalid category: {category_name}'}
            category_obj = self.Category.get(name=category_name, type=operation_obj)

            if not self.Subcategory.filter(name=subcategory_name, category=category_obj).exists():
                return {'is_edited': False, 'message': f'Invalid subcategory: {subcategory_name}'}
            subcategory_obj = self.Subcategory.get(name=subcategory_name, category=category_obj)

            transaction_obj.status = status_obj
            transaction_obj.type = operation_obj
            transaction_obj.category = category_obj
            transaction_obj.subcategory = subcategory_obj
            transaction_obj.amount = amount
            transaction_obj.comment = comment

            transaction_obj.save()

            return {'is_edited': True, 'message': f'Transaction edited successfully'}
        except Exception as e:
            return {'is_edited': False, 'message': str(e)}
