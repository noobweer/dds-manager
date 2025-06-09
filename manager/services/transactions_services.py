from ..models import *


class TransactionsService:
    def __init__(self):
        self.Transaction = Transaction.objects
        self.Status = Status.objects
        self.OperationType = OperationType.objects
        self.Category = Category.objects
        self.Subcategory = Subcategory.objects

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
