# config/settings.py

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",  # Aponta para o .env diretamente
        case_sensitive=True,  # Sensibilidade a maiúsculas/minúsculas
        extra="allow"  # Permite variáveis extras no .env
    )

# Instância global de configuração para ser importada
settings = Settings()


