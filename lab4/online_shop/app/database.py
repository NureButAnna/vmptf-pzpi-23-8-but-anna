from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

username = "postgres"
password = "anna.1208"
host = "localhost"
port = 5432
db_name = "shop_db"

DATABASE_URL = (
    f"postgresql+psycopg2://{username}:{password}"
    f"@{host}:{port}/{db_name}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

try:
    with engine.connect() as connection:
        print("Connected!")
except Exception as e:
    print("Connection error:", e)