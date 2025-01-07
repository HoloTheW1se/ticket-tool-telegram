from typing import Dict, List, TypeVar

from database.common.models import db

T = TypeVar('T')


def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    """
    Сохранение данных в базу данных

    :param db: Объект БД
    :param model: Модель БД
    :param data: Данные для загрузки
    :return: None
    """
    with db.atomic():
        model.insert_many(*data).execute()


class Crud_interface:
    """
    Интерфейс для взаимодействия с БД
    """
    @staticmethod
    def create():
        """
        Загрузка данных
        :return: None
        """
        return _store_date


if __name__ == '__main__':
    _store_date()
    Crud_interface()
