from flask import Blueprint
from flask_restful import Api

# Create a Blueprint for API version 1
api_routes = Blueprint('api_v1', __name__)
api = Api(api_routes)

# Use lazy imports to avoid circular dependencies
def register_routes():
    from .auth import AuthResource
    from .order import OrderResource
    from .notification import NotificationResource  # Import inside function

    # Register API Resources
    api.add_resource(AuthResource, '/auth')
    api.add_resource(OrderResource, '/order')
    api.add_resource(NotificationResource, '/notification')
