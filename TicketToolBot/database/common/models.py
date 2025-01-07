from datetime import datetime
from settings import db_path
import peewee as pw

db = pw.SqliteDatabase(db_path)


class Base_model(pw.Model):
    created_at = pw.DateTimeField(default=datetime.now())

    class Meta:
        database = db


class User(Base_model):
    user_id = pw.IntegerField(primary_key=True)
    username = pw.CharField()
    first_name = pw.CharField()
    last_name = pw.CharField(null=True)


class Ticket(Base_model):
    id = pw.AutoField()
    user = pw.ForeignKeyField(User, backref="user_ticket")
    chat_id = pw.TextField()
