from main.extension.extension import db

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


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
