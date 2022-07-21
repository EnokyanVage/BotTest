from sqlalchemy import BigInteger, Column, Float, String, sql

from utils.database_api.db_publicplaces import TimedBaseModel


class PubliPlace(TimedBaseModel):
    __tablename__ = 'public_place'
    pp_id = Column(BigInteger, primary_key=True)
    pp_name = Column(String(200))
    phone_number = Column(String(12))
    location = Column(String(25))
    atl = Column(String(256))
    work_time = Column(String(25))
    category = Column(String(10))
    photo = Column(String(64))
    link = Column(String(64))
    rating = Column(Float(7))

    query: sql.select