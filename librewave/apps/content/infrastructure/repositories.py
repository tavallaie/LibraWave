from typing import List
from sqlmodel import Session, select
from apps.content.domain.models import Content


class ContentRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, content: Content):
        self.session.add(content)
        self.session.commit()
        self.session.refresh(content)
        return content

    def get(self, content_id: int) -> Content:
        content = self.session.get(Content, content_id)
        if not content:
            raise ValueError("Content not found")
        return content

    def get_all(self) -> List[Content]:
        return self.session.exec(select(Content)).all()

    def update(self, content_id: int, content_data: dict) -> Content:
        content = self.session.get(Content, content_id)
        if not content:
            raise ValueError("Content not found")
        for key, value in content_data.items():
            setattr(content, key, value)
        self.session.add(content)
        self.session.commit()
        self.session.refresh(content)
        return content

    def delete(self, content_id: int) -> None:
        content = self.session.get(Content, content_id)
        if not content:
            raise ValueError("Content not found")
        self.session.delete(content)
        self.session.commit()
