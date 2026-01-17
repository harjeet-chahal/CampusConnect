from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class ChatMessage(Base):
    content = Column(String, nullable=False)
    
    sender_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("event.id"), nullable=False)
    
    # Relationships
    sender = relationship("User", back_populates="messages")
    event = relationship("Event", back_populates="messages")
