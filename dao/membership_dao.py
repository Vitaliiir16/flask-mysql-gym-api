from.db_connector import get_cursor

def create_membership(client_id, membership_type, start_date, end_date):
    with get_cursor() as cursor:
        query = "INSERT INTO Memberships (client_id, membership_type, start_date, end_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (client_id, membership_type, start_date, end_date))
        return cursor.lastrowid

def get_all_memberships():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Memberships")
        return cursor.fetchall()

def get_membership_by_id(membership_id):
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Memberships WHERE membership_id = %s", (membership_id,))
        return cursor.fetchone()

def update_membership(membership_id, client_id, membership_type, start_date, end_date):
    with get_cursor() as cursor:
        query = "UPDATE Memberships SET client_id = %s, membership_type = %s, start_date = %s, end_date = %s WHERE membership_id = %s"
        cursor.execute(query, (client_id, membership_type, start_date, end_date, membership_id))
        return cursor.rowcount > 0

def delete_membership(membership_id):
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM Memberships WHERE membership_id = %s", (membership_id,))
        return cursor.rowcount > 0