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

class DaySchedule(Base):
    __tablename__ = "daySchedules"
    #La primery key podría ser el id del usuario con day. Ejemplo: 1-monday, 1-tuesday, 1-wednesday, etc.
    id = Column(Integer, primary_key=True, index=True)
    day = Column(Enum(Day), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="day_schedules") #Falta agregar el back_populates en el modelo User
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

