from ..models import *
from ..serializers import *


class CategoryService:
    def __init__(self):
        self.Category = Category.objects
        self.OperationType = OperationType.objects

    def create_category(self, data):
        try:
            category_name = data.get('name')
            type_id = data.get('type_id')

            if not all([category_name, type_id]):
                return {'is_created': False,
                        'message': 'Send all required fields (name, type_id)'}

            if not self.OperationType.filter(id=type_id).exists():
                return {'is_created': False, 'message': f'Invalid type_id ({type_id})'}
            type_obj = self.OperationType.get(id=type_id)

            if self.Category.filter(name=category_name, type=type_obj).exists():
                return {'is_created': False, 'message': f'Category already exists ({category_name}, {type_id})'}

            self.Category.create(name=category_name, type=type_obj)

            return {'is_created': True, 'message': f'Category created successfully'}
        except Exception as e:
            return {'is_created': False, 'message': str(e)}

    def edit_category(self, data):
        try:
            category_id = data.get('id')
            category_name = data.get('name')
            type_id = data.get('type_id')

            if not all([category_id, category_name, type_id]):
                return {'is_edited': False,
                        'message': 'Send all required fields (id, name, type_id)'}

            if not self.Category.filter(id=category_id).exists():
                return {'is_edited': False, 'message': f'Invalid category_id ({category_id})'}
            category_obj = self.Category.get(id=category_id)

            if not self.OperationType.filter(id=type_id).exists():
                return {'is_edited': False, 'message': f'Invalid type_id ({type_id})'}
            type_obj = self.OperationType.get(id=type_id)

            category_obj.name = category_name
            category_obj.type = type_obj

            category_obj.save()

            return {'is_edited': True, 'message': 'Category edited successfully'}
        except Exception as e:
            return {'is_edited': False, 'message': str(e)}

    def delete_category(self, data):
        category_id = data.get('id')

        if not all([category_id]):
            return {'is_deleted': False,
                    'message': 'Send all required fields (id)'}

        if not self.Category.filter(id=category_id).exists():
            return {'is_deleted': False, 'message': f'Invalid category_id ({category_id})'}

    def all_categories(self):
        try:
            categories = Category.objects.select_related('type').all()
            serializer = CategorySerializer(categories, many=True)
            return {'success': True, 'categories': serializer.data}
        except Exception as e:
            print(e)
            return {'success': False, 'categories': []}
