# main/models.py
import bcrypt
from main.extension.extension import db
from marshmallow import Schema, fields, validates, ValidationError

# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
class User(db.Model):
    __tablename__ = 'users1'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(15))
    photo = db.Column(db.String(255))
    address = db.Column(db.String(255))
    password = db.Column(db.String(120), nullable=False)
    account_status = db.Column(db.String(1), default='1')  # '1' for active, '2' for suspended
    user_type = db.Column(db.String(1), default='1')  # '1' for regular user, '2' for admin

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'username': self.username
    #     }

# class UserSchema(Schema):
#     id = fields.Int(dump_only=True)
#     username = fields.Str(required=True)
#     password = fields.Str(load_only=True, required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    name = fields.Str()
    email = fields.Str()
    phone_number = fields.Str()
    photo = fields.Str()
    address = fields.Str()
    account_status = fields.Str()
    user_type = fields.Str()
    
    @validates('username')
    def validate_username(self, value):
        if not value:
            raise ValidationError('Username is required.')

    @validates('password')
    def validate_password(self, value):
        if not value or len(value) < 6:
            raise ValidationError('Password must be at least 6 characters long.')

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
