from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token
from main.database.models import User, db
from main.schemas import UserSchema
from main.extension.extension import bcrypt  # Ensure this is initialized properly

# Blueprint for authentication
auth_blueprint = Blueprint('auth', __name__)

# @auth_blueprint.route('/signup', methods=['POST'])
# def signup():
#     data = request.get_json()
#     user_schema = UserSchema()

#     try:
#         user_data = user_schema.load(data)
#     except Exception as e:
#         return jsonify({"message": "Invalid data", "error": str(e)}), 400

#     if User.query.filter_by(username=user_data['username']).first():
#         return jsonify({"message": "User already exists"}), 400

#     hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
#     new_user = User(username=user_data['username'], password=hashed_password)

#     try:
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify({'message': 'User created successfully!'}), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

# @auth_blueprint.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user_schema = UserSchema()

#     try:
#         user_data = user_schema.load(data)
#     except Exception as e:
#         return jsonify({"message": "Invalid data", "error": str(e)}), 400

#     user = User.query.filter_by(username=user_data['username']).first()
#     if user and bcrypt.check_password_hash(user.password, user_data['password']):
#         access_token = create_access_token(identity=user.username)
#         return jsonify({'message': 'Login successful', 'access_token': access_token}), 200
#     else:
#         return jsonify({'message': 'Invalid credentials'}), 401
class signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        name = data.get('name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        photo = data.get('photo')
        address = data.get('address')
        password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
        
        if not data.get('username') or not data.get('password') or not data.get('email'):
            return {"message": "Username, email, and password are required"}, 400
        
        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 400
        
        new_user = User(
            username=username,
            name=name,
            email=email,
            phone_number=phone_number,
            photo=photo,
            address=address,
            password=password
        )
        print("New User:", new_user)
        db.session.add(new_user)
        db.session.commit()
       
        return jsonify({
            'message': 'User created successfully',
            'status': '1',
        })
        
class login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not data.get('email') or not data.get('password'):
            return {"message": "Email and Password are required"}, 400
    
    # Check if user exists
        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not bcrypt.check_password_hash(user.password, data['password']):
            return {"message": "Invalid credentials"}, 401
        
        access_token = create_access_token(identity={'username': username})
        
        response_data = {
                        "code": 200,
            "message": "Login successfully",
            "status": 1,
            "token": access_token,
            "data": {
            "id": user.id,
            "full_name": user.name,
            "email": user.email,
            "account_status": user.account_status,
            "user_type": user.user_type,
            "profile_pic": user.photo or "",
            }
        }
        
        return (response_data), 200
api = Api(auth_blueprint)
api.add_resource(signup, '/signup')
api.add_resource(login, '/login')
