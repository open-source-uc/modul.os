from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean, Text
from sqlalchemy.orm import relationship
import enum

class Day(enum.Enum):
    monday = 1
    tuesday = 2
    wednesday = 3
    thursday = 4
    friday = 5


DayEnum = Enum(Day, name='day_enum', create_type=False)

class DaySchedule(Base):
    __tablename__ = "daySchedules"
    id = Column(Integer, primary_key=True, index=True)
    day = Column(DayEnum, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="day_schedules")
    block_day_schedules = relationship("BlockDaySchedule", back_populates="day_schedule")
    
class BlockDaySchedule(Base):
    __tablename__ = "blockDaySchedules"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(String)
    end_time = Column(String)
    title = Column(String)
    description = Column(Text)
    availability = Column(Boolean)
    day_schedule_id = Column(Integer, ForeignKey("daySchedules.id"), nullable=False)
    day_schedule = relationship("DaySchedule", back_populates="block_day_schedules")
    meetings = relationship("Meeting", back_populates="block_day_schedule")
