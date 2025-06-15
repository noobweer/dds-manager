from ..models import *
from ..serializers import *


class SubcategoryService:
    def __init__(self):
        self.Subcategory = Subcategory.objects
        self.Category = Category.objects

    def create_subcategory(self, data):
        try:
            subcategory_name = data.get('name')
            category_id = data.get('category_id')

            if not all([subcategory_name, category_id]):
                return {'is_created': False,
                        'message': 'Send all required fields (name, category_id)'}

            if not self.Category.filter(id=category_id).exists():
                return {'is_created': False, 'message': f'Invalid category_id ({category_id})'}
            category_obj = self.Category.get(id=category_id)

            if self.Subcategory.filter(name=subcategory_name, category=category_obj).exists():
                return {'is_created': False, 'message': f'Subcategory already exists ({subcategory_name}, {category_id})'}

            self.Subcategory.create(name=subcategory_name, category=category_obj)

            return {'is_created': True, 'message': f'Subcategory created successfully'}
        except Exception as e:
            return {'is_created': False, 'message': str(e)}

    def edit_subcategory(self, data):
        try:
            subcategory_id = data.get('id')
            subcategory_name = data.get('name')
            category_id = data.get('category_id')

            if not all([subcategory_id, subcategory_name, category_id]):
                return {'is_edited': False,
                        'message': 'Send all required fields (id, name, category_id)'}

            if not self.Subcategory.filter(id=subcategory_id).exists():
                return {'is_edited': False, 'message': f'Invalid subcategory_id ({subcategory_id})'}
            subcategory_obj = self.Subcategory.get(id=subcategory_id)

            if not self.Category.filter(id=category_id).exists():
                return {'is_edited': False, 'message': f'Invalid category_id ({category_id})'}
            category_obj = self.Category.get(id=category_id)

            subcategory_obj.name = subcategory_name
            subcategory_obj.category = category_obj

            subcategory_obj.save()

            return {'is_edited': True, 'message': f'Subcategory edited successfully'}
        except Exception as e:
            return {'is_edited': False, 'message': str(e)}

    def delete_subcategory(self, data):
        try:
            subcategory_id = data.get('id')

            if not all([subcategory_id]):
                return {'is_deleted': False,
                        'message': 'Send all required fields (id, name, category_id)'}

            if not self.Subcategory.filter(id=subcategory_id).exists():
                return {'is_deleted': False, 'message': f'Invalid subcategory_id ({subcategory_id})'}

            self.Subcategory.filter(id=subcategory_id).delete()

            return {'is_deleted': True, 'message': f'Subcategory deleted successfully'}
        except Exception as e:
            return {'is_deleted': False, 'message': str(e)}

    def all_subcategories(self):
        try:
            subcategories = Subcategory.objects.select_related('category').all()
            serializer = SubcategorySerializer(subcategories, many=True)
            return {'success': True, 'subcategories': serializer.data}
        except Exception as e:
            print(e)
            return {'success': False, 'subcategories': []}
