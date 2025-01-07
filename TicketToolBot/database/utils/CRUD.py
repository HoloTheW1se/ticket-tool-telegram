from typing import Dict, List, TypeVar

from database.common.models import db

T = TypeVar('T')


def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).execute()


class Crud_interface:
    @staticmethod
    def create():
        return _store_date


if __name__ == '__main__':
    _store_date()
    Crud_interface()
