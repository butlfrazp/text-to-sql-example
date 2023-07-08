import os
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    _db_uri: str
    _openai_api_type: str

    def __init__(self):
        db_uri = os.getenv("DB_URI")
        openai_api_type = os.getenv("OPENAI_API_TYPE", "open_ai")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        openai_api_base = os.getenv("OPENAI_API_BASE")
        openai_api_version = os.getenv("OPENAI_API_VERSION")

        if db_uri is None:
            raise ValueError("DB_URI is not set")

        if openai_api_type is None:
            raise ValueError("OPENAI_API_TYPE is not set")

        if openai_api_key is None:
            raise ValueError("OPENAI_API_KEY is not set")

        self._openai_api_type = openai_api_type
        self._db_uri = db_uri

        # validate the azure openai api config
        if self.is_azure_openai_api and openai_api_base is None:
            raise ValueError("OPENAI_API_BASE is not set")

        if self.is_azure_openai_api and openai_api_version is None:
            raise ValueError("OPENAI_API_VERSION is not set")

    @property
    def is_azure_openai_api(self) -> bool:
        return self._openai_api_type.lower() == "azure"

    @property
    def db_uri(self) -> str:
        return self._db_uri


config = Config()
