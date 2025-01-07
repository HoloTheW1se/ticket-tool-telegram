from database.utils.CRUD import Crud_interface
from database.common.models import db, Base_model


if __name__ == '__main__':
    db.connect()
    db.create_tables(Base_model.__subclasses__())
    crud = Crud_interface()
    crud()
