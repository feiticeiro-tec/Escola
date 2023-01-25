from flask import Flask
import dotenv

dotenv.load_dotenv('.env')


class Servidor(Flask):
    from .api import init_api
    from .database import init_db

    def __init__(self):
        super().__init__(__name__)

        with self.app_context():
            self.config.from_prefixed_env()
            self.api = self.init_api()
            self.db = self.init_db()
