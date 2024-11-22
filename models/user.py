from sqlalchemy import Column, Integer, String, Boolean
from ..config.config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
