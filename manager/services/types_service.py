from ..models import *
from ..serializers import *


class OperationTypeService:
    def __init__(self):
        self.OperationType = OperationType.objects

    def create_type(self, data):
        try:
            type_name = data.get('name')

            if not all([type_name]):
                return {'is_created': False,
                        'message': 'Send all required fields (name)'}

            if self.OperationType.filter(name=type_name).exists():
                return {'is_created': False, 'message': f'Operation type already exists ({type_name})'}

            self.OperationType.create(name=type_name)
            return {'is_created': True, 'message': 'Operation type created successfully'}
        except Exception as e:
            return {'is_created': False, 'message': str(e)}

    def edit_type(self, data):
        try:
            type_id = data.get('id')
            type_name = data.get('name')

            if not all([type_id, type_name]):
                return {'is_edited': False,
                        'message': 'Send all required fields (id, name)'}

            if not self.OperationType.filter(id=type_id).exists():
                return {'is_edited': False, 'message': f'Invalid type_id ({type_id})'}
            type_obj = self.OperationType.get(id=type_id)

            if (type_obj.name != type_name) and (self.OperationType.filter(name=type_name).exists()):
                return {'is_edited': False, 'message': f'Operation type with this name already exists ({type_id}, {type_name})'}

            type_obj.name = type_name
            type_obj.save()

            return {'is_edited': True, 'message': f'Operation type edited successfully'}
        except Exception as e:
            return {'is_edited': False, 'message': str(e)}

    def delete_type(self, data):
        try:
            type_id = data.get('id')

            if not all([type_id]):
                return {'is_created': False,
                        'message': 'Send all required fields (id)'}

            if not self.OperationType.filter(id=type_id).exists():
                return {'is_deleted': False, 'message': f'Invalid type_id ({type_id})'}

            self.OperationType.filter(id=type_id).delete()

            return {'is_delete': True, 'message': f'Operation type deleted successfully'}
        except Exception as e:
            return {'is_edited': False, 'message': str(e)}

    def all_types(self):
        try:
            types = self.OperationType.all()
            serializer = OperationTypeSerializer(types, many=True)

            return {'success': True, 'types': serializer.data}
        except Exception as e:
            print(e)
            return {'success': False, 'types': []}
