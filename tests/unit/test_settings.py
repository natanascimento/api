import pytest
from unittest.mock import patch


@pytest.fixture
def set_env_vars(monkeypatch):
    monkeypatch.setenv('DB_TYPE', 'mock_db_type')
    monkeypatch.setenv('DB_USER', 'mock_db_user')
    monkeypatch.setenv('DB_PASSWORD', 'mock_db_password')
    monkeypatch.setenv('DB_CLUSTER', 'mock_db_cluster')
    monkeypatch.setenv('DB_NAME', 'mock_db_name')
    monkeypatch.setenv('ENV', 'dev')


@patch('dotenv.load_dotenv')
@patch('dotenv.find_dotenv', return_value='/path/to/.env')
def test_database_settings_should_be_correct(mock_find_dotenv, mock_load_dotenv, set_env_vars):

    from app.core.config.settings import DatabaseSettings

    settings = DatabaseSettings()
    assert settings.DB_TYPE == 'mock_db_type'
    assert settings.DB_USER == 'mock_db_user'
    assert settings.DB_PASSWORD == 'mock_db_password'
    assert settings.DB_CLUSTER == 'mock_db_cluster'
    assert settings.DB_NAME == 'mock_db_name'


@patch('dotenv.load_dotenv')
@patch('dotenv.find_dotenv', return_value='/path/to/.env')
def test_app_settings_should_be_correct(mock_find_dotenv, mock_load_dotenv, set_env_vars):
    
    from app.core.config.settings import AppSettings

    settings = AppSettings()
    assert settings.APP_NAME == "API Template for XPTO"
    assert settings.ENV == 'dev'


@patch('dotenv.load_dotenv')
@patch('dotenv.find_dotenv', return_value='/path/to/.env')
def test_settings_should_be_correct(mock_find_dotenv, mock_load_dotenv, set_env_vars):
    
    from app.core.config.settings import Settings

    settings = Settings()
    assert settings.app.APP_NAME == "API Template for XPTO"
    assert settings.app.ENV == 'dev'
    assert settings.database.DB_TYPE == 'mock_db_type'
    assert settings.database.DB_USER == 'mock_db_user'
    assert settings.database.DB_PASSWORD == 'mock_db_password'
    assert settings.database.DB_CLUSTER == 'mock_db_cluster'
    assert settings.database.DB_NAME == 'mock_db_name'