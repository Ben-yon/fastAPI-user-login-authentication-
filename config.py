import os


class Config:
    username = os.getenv("DB_USERNAME", "postgres")
    password = os.getenv("DB_PASSWORD", "postgres")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "fastapi")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"
    )


SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI
