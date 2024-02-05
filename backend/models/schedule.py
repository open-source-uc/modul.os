from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean, Text
from sqlalchemy.orm import relationship
import enum

class Day(enum.Enum):
    monday = 1
    tuesday = 2
    wednesday = 3
    thursday = 4
    friday = 5

class DaySchedule(Base):
    __tablename__ = "daySchedules"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(Enum(Day))
    BlockDaySchedules = relationship("BlockDaySchedule", back_populates="daySchedule")
    
class BlockDaySchedule(Base):
    __tablename__ = "blockDaySchedules"

    id = Column(Integer, primary_key=True, index=True)
    block = Column(Integer)
    start_time = Column(String)
    end_time = Column(String)
    description = Column(Text)
    availability = Column(Boolean)
    daySchedule_id = Column(Integer, ForeignKey("daySchedules.id"), nullable=False)
    daySchedule = relationship("DaySchedule", back_populates="blockDaySchedules")