from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


@contextmanager
def managed_ro_session() -> Generator[Session]:

    # Format: postgresql+driver://user:password@host:port/dbname
    engine = create_engine("recommender_user:recommender_pass@0.0.0.0:5433/recommender")
    session_maker = sessionmaker(engine)
    with session_maker() as session:
        try:
            yield session
        except:
            session.rollback()
            raise
        else:
            session.commit()