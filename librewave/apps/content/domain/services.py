from typing import List
from sqlmodel import Session, select
from apps.content.domain.models import Content


class ContentService:
    def create_content(self, session: Session, content_data: dict) -> Content:
        content = Content(**content_data)
        session.add(content)
        session.commit()
        session.refresh(content)
        return content

    def get_content(self, session: Session, content_id: int) -> Content:
        content = session.get(Content, content_id)
        if not content:
            raise ValueError("Content not found")
        return content

    def get_all_contents(self, session: Session) -> List[Content]:
        return session.exec(select(Content)).all()

    def update_content(
        self, session: Session, content_id: int, content_data: dict
    ) -> Content:
        content = session.get(Content, content_id)
        if not content:
            raise ValueError("Content not found")
        for key, value in content_data.items():
            setattr(content, key, value)
        session.add(content)
        session.commit()
        session.refresh(content)
        return content

    def delete_content(self, session: Session, content_id: int) -> None:
        content = session.get(Content, content_id)
        if not content:
            raise ValueError("Content not found")
        session.delete(content)
        session.commit()
