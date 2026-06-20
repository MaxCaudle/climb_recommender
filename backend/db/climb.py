from sqlalchemy import Column, String, Float, INTEGER

from backend.db.base import Base


class Climb(Base):
    __tablename__ = 'climb'

    name = Column('name', String, nullable=False)
    area_id = Column('area_id', INTEGER, nullable=False, foreign_key='area.id')
    average_grade = Column('average_grade', Float, nullable=False)
    flash_rate = Column('flash_rate', Float, nullable=False)
    average_rating = Column('average_rating', Float, nullable=False)
    total_ascents = Column('total_ascents', INTEGER, nullable=False)
    recommended_rate = Column('recommended_rate', Float, nullable=False)
    jan_ascents = Column('jan_ascents', INTEGER, nullable=False)
    feb_ascents = Column('feb_ascents', INTEGER, nullable=False)
    mar_ascents = Column('mar_ascents', INTEGER, nullable=False)
    apr_ascents = Column('apr_ascents', INTEGER, nullable=False)
    may_ascents = Column('may_ascents', INTEGER, nullable=False)
    jun_ascents = Column('jun_ascents', INTEGER, nullable=False)
    jul_ascents = Column('jul_ascents', INTEGER, nullable=False)
    aug_ascents = Column('aug_ascents', INTEGER, nullable=False)
    sep_ascents = Column('sep_ascents', INTEGER, nullable=False)
    oct_ascents = Column('oct_ascents', INTEGER, nullable=False)
    nov_ascents = Column('nov_ascents', INTEGER, nullable=False)
    dec_ascents = Column('dec_ascents', INTEGER, nullable=False)
