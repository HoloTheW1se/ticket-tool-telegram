from database.utils.CRUD import Crud_interface
from database.common.models import db, Base_model

db.connect()
db.create_tables(Base_model.__subclasses__())

crud = Crud_interface()

if __name__ == '__main__':
    crud()
