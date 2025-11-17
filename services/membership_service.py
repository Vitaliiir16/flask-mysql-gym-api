from dao import membership_dao, client_dao
from datetime import date

def _convert_dates(membership):
    if membership:
        if 'start_date' in membership and isinstance(membership['start_date'], date):
            membership['start_date'] = membership['start_date'].isoformat()
        if 'end_date' in membership and isinstance(membership['end_date'], date):
            membership['end_date'] = membership['end_date'].isoformat()
    return membership

def _validate_foreign_keys(data):
    if 'client_id' in data and data['client_id'] is not None:
        if not client_dao.get_client_by_id(data['client_id']):
            raise ValueError(f"Invalid client_id: Client {data['client_id']} does not exist.")

def create_membership(data):
    _validate_foreign_keys(data)
    return membership_dao.create_membership(
        data['client_id'], data['membership_type'], data['start_date'], data['end_date']
    )

def get_all_memberships():
    memberships = membership_dao.get_all_memberships()
    return [_convert_dates(m) for m in memberships]

def get_membership_by_id(membership_id):
    membership = membership_dao.get_membership_by_id(membership_id)
    if not membership:
        raise ValueError("Membership not found")
    return _convert_dates(membership)

def update_membership(membership_id, data):
    if not membership_dao.get_membership_by_id(membership_id):
        raise ValueError("Membership not found")
    _validate_foreign_keys(data)
    return membership_dao.update_membership(
        membership_id, data['client_id'], data['membership_type'], data['start_date'], data['end_date']
    )

def delete_membership(membership_id):
    if not membership_dao.get_membership_by_id(membership_id):
        raise ValueError("Membership not found")
    return membership_dao.delete_membership(membership_id)