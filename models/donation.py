from models.base_model import BaseModel
from models.user import User
import peewee as pw


class Donation(BaseModel):
    user = pw.ForeignKeyField(User, backref='donation')
    amount = pw.DecimalField()
