from marshmallow import Schema, fields, validates, ValidationError

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

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)

    @validates('name')
    def validate_name(self, value):
        if not value or len(value) < 3:
            raise ValidationError('Name must be at least 3 characters long.')

    @validates('description')
    def validate_description(self, value):
        if not value:
            raise ValidationError('Description is required.')
