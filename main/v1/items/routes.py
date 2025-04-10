from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from main.database.models import Item, db
from main.schemas import ItemSchema

items_blueprint = Blueprint('items', __name__)
api = Api(items_blueprint)

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)

class ItemResource(Resource):
    def get(self, id):
        item = Item.query.get_or_404(id)
        if item:
            status = 1 
            message = "Item fetched successfully"
        else:
            status = 0
            message = "Item not found"
        print(f"Item found: {item}")  # Debug output to check item
        return {
                    "status": status,
                    "message": message,
                    "data": item_schema.dump(item)
            }, 200
        
    def put(self, id):
        item = Item.query.get_or_404(id)
        data = request.get_json()
        errors = item_schema.validate(data)
        if errors:
            return {
                "status": 0,
                "message": "Failed to update item",
                "error": errors
            }, 400
        item.name = data['name']
        item.description = data['description']
        db.session.commit()
        return {
            "status": 1,
            "message": "Item updated successfully",
            "data": item_schema.dump(item)
        }, 200

    def delete(self, id):
        item = Item.query.get_or_404(id)
        if not item:
            return {
                "status": 0,
                "message": "Item not found"
            }, 404
        print(f"Deleting item: {item}")
        db.session.delete(item)
        db.session.commit()
        return jsonify({
            "status": 1,
            "message": "Item deleted successfully"
        }), 204
        
        
class ItemListResource(Resource):
    def get(self):
        items = Item.query.all()
        if items:
            status = 1 
            message = "Items fetched successfully"
        else:
            status = 0
            message = "No items found"
        print(f"Items found: {items}")  # Debug output to check items
        return {
                    "status": status,
                    "message": message,
                    "data": item_list_schema.dump(items)
            }, 200
        
    def post(self):
        data = request.get_json()
        errors = item_schema.validate(data)
        if errors:
            return {
                "status": 0,
                "message": "Failed to create item",
                "error": errors
            }, 400

        new_item = Item(name=data['name'], description=data['description'])
        db.session.add(new_item)
        db.session.commit()

        return {
            "status": 1,
            "message": "Item created successfully",
            "data": item_schema.dump(new_item)
        }, 201


api.add_resource(ItemResource, '/<int:id>')
api.add_resource(ItemListResource, '/')
