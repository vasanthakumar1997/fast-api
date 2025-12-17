from mongoengine import Document, connect, StringField, DateField
import bcrypt

connect(db='test_db',host='localhost',port=27017)

class User(Document):
    name = StringField(max_length=100,required=True)
    address = StringField(max_length=400)
    email = StringField(max_length=100,unique=True)
    dob = DateField(required=True)
    password = StringField(required=True)

    def set_password(self, raw_password: str):
        """Hash password before saving"""
        hashed = bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt())
        self.password = hashed.decode("utf-8")

    def check_password(self, raw_password: str) -> bool:
        """Verify password"""
        return bcrypt.checkpw(raw_password.encode("utf-8"), self.password.encode("utf-8"))
