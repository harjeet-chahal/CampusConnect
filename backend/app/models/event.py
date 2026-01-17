from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum

from app.db.base_class import Base

class ParticipantStatus(str, enum.Enum):
    GOING = "going"
    INTERESTED = "interested"
    NOT_GOING = "not_going"

class Event(Base):
    title = Column(String, index=True, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    capacity = Column(Integer, nullable=True) # None means unlimited
    
    creator_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    
    # Relationships
    creator = relationship("User", back_populates="events_created")
    participants = relationship("EventParticipant", back_populates="event", cascade="all, delete-orphan")
    messages = relationship("ChatMessage", back_populates="event", cascade="all, delete-orphan")

class EventParticipant(Base):
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("event.id"), nullable=False)
    status = Column(SQLEnum(ParticipantStatus), default=ParticipantStatus.INTERESTED, nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="event_participations")
    event = relationship("Event", back_populates="participants")
