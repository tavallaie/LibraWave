from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = (
    "sqlite:///./librewave.db"  # Use an appropriate database URL for your setup
)
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
