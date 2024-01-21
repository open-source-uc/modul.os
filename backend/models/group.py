from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean, Text
from sqlalchemy.orm import relationship
import enum

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    users = relationship("User", secondary="groupUsers", back_populates="groups")
    group_schedules = relationship("GroupSchedule", back_populates="group")

class GroupUser(Base):
    __tablename__ = "groupUsers"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)