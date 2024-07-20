from os.path import abspath, dirname, join
from os import environ
import dotenv


class DatabaseSettings:
    DB_TYPE = environ.get('DB_TYPE')
    DB_USER = environ.get('DB_USER')
    DB_PASSWORD = environ.get('DB_PASSWORD')
    DB_CLUSTER = environ.get('DB_CLUSTER')
    DB_NAME = environ.get('DB_NAME')

class AppSettings:
    APP_NAME = "API Template for XPTO"
    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    PROJECT_PATH = dirname(dirname(dirname(abspath(__file__))))
    LOGS_PATH = join(ROOT_PATH, "logs")
    ENV = environ.get('ENV')

class Settings:
    dotenv.load_dotenv(dotenv.find_dotenv())
    app: AppSettings = AppSettings()
    database: DatabaseSettings = DatabaseSettings()



