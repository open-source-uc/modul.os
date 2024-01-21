from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean, Text, DateTime
from sqlalchemy.orm import relationship
import enum

class Meeting(Base):
    __tablename__ = "meetings"
    
    id = Column(Integer, primary_key=True, index=True)
    notes = Column(Text)
    date = Column(DateTime)
    block_day_schedule_id = Column(Integer, ForeignKey("blockDaySchedules.id"), nullable=False)
    block_day_schedule = relationship("BlockDaySchedule", back_populates="meetings")