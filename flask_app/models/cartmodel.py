from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Cart:
    def __init__(self,data):
        self.id = data['id']
        self.quantity = data['quantity']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data ['user_id']

    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM products WHERE id = %(id)s;'
        return connectToMySQL('project_schema').query_db(query,data)

