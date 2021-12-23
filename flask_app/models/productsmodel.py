from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Product:
    def __init__(self,data):
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.category_id = data['category_id']

    @classmethod
    def get_all_category(cls): #input data later 
        query = 'SELECT * FROM products WHERE category_id = 1;'
        results = connectToMySQL('project_schema').query_db(query)
        products = []
        if results:
            for item in results:
                products.append(cls(item))
        return products