from ..models import *


class StatusesService:
    def __init__(self):
        self.Status = Status.objects

    def create_status(self, data):
        try:
            status_name = data.get('name')

            if not all([status_name]):
                return {'is_created': False,
                        'message': 'Send all required fields (name)'}

            if self.Status.filter(name=status_name).exists():
                return {'is_created': False, 'message': f'Status already exists ({status_name})'}

            self.Status.create(name=status_name)
            return {'is_created': True, 'message': 'Status created successfully'}
        except Exception as e:
            return {'is_created': False, 'message': str(e)}

    def edit_status(self, data):
        try:
            status_id = data.get('id')
            status_name = data.get('name')

            if not all([status_id, status_name]):
                return {'is_edited': False,
                        'message': 'Send all required fields (id, name)'}

            if not self.Status.filter(id=status_id).exists():
                return {'is_edited': False, 'message': f'Invalid status_id ({status_id})'}
            status_obj = self.Status.get(id=status_id)

            if (status_obj.name != status_name) and (self.Status.filter(name=status_name).exists()):
                return {'is_edited': False, 'message': f'Status with this name already exists ({status_id}, {status_name})'}

            status_obj.name = status_name
            status_obj.save()

            return {'is_edited': True, 'message': f'Status edited successfully'}
        except Exception as e:
            return {'is_edited': False, 'message': str(e)}

    def delete_status(self, data):
        try:
            status_id = data.get('id')

            if not all([status_id]):
                return {'is_created': False,
                        'message': 'Send all required fields (id)'}

            if not self.Status.filter(id=status_id).exists():
                return {'is_deleted': False, 'message': f'Invalid status_id ({status_id})'}

            self.Status.filter(id=status_id).delete()

            return {'is_delete': True, 'message': f'Status deleted successfully'}
        except Exception as e:
            return {'is_edited': False, 'message': str(e)}