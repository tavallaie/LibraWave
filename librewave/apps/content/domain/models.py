from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Content(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: Optional[str]
    content_type: str  # e.g., "book", "paper", "blog", "markdown"
    content: str
    link: Optional[str] = None
    file_path: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
