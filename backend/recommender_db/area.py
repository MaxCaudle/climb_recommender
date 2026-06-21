from sqlalchemy import Column, String

from backend.recommender_db.base import Base


class Area(Base):
    __tablename__ = 'area'

    name = Column('name', String, nullable=False)
    crag_slug = Column('crag_slug', String, nullable=False)
    country_name = Column('country_name', String, nullable=False)
    sector_name = Column('sector_name', String, nullable=True)
    area_name = Column('area_name', String, nullable=True)