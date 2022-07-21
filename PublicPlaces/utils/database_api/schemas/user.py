from sqlalchemy import BigInteger, Column, String, sql

from utils.database_api.db_publicplaces import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(200), primary_key=True)

    query: sql.select