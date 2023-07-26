from infra.configs.connection import DBConnectionHandler
from infra.entities.experimento import Experimento


class ExperimentoRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Experimento).all()
            return data

    def insert(self, click, visit, grupo):
        with DBConnectionHandler() as db:
            data_insert = Experimento(click=click, visit=visit, grupo=grupo)
            db.session.add(data_insert)
            db.session.commit()