# Imports
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from .database import Base

# Create cls Post with inherit
class Post(Base):
    # Init table name for db
    __tablename__ = 'posts'

    # Init table columns
    #     primary_key - уникальный ключ для записей
    #     nullable - can be column value is empty?
    #     server_default - default value column
    #     TIMESTAMP - тип данных (time)
    #         timezone - указывает зону, где было это время
    id = Column(Integer, primary_key=True,  nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)