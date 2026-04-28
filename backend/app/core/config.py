from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #connexion postgresql 
    DATABASE_URL:str

    #securite JWT
    SECRET_KEY:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    ALGORITHM:str
    
    #conf intern
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
 #instancier la classe    
settings=Settings()