import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path


class DBConnectionHandler:
    def __init__(self):
        dotenv_path = Path('/etc/secrets/.env')
        load_dotenv(dotenv_path=dotenv_path)

        url = os.getenv('DATABASE_URL')
        self.__connection_string = url
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        ssesion_make = sessionmaker(bind=self.__engine)
        self.session = ssesion_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
