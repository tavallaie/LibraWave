from typing import List
from apps.content.infrastructure.database import get_session
from apps.content.infrastructure.repositories import ContentRepository
from apps.content.domain.models import Content
from apps.content.domain.services import ContentService


class ContentManager:
    def __init__(self):
        self.session = next(get_session())
        self.repository = ContentRepository(self.session)
        self.service = ContentService()

    def create_content(self, content_data: dict) -> Content:
        return self.service.create_content(self.session, content_data)

    def get_content(self, content_id: int) -> Content:
        return self.service.get_content(self.session, content_id)

    def get_all_contents(self) -> List[Content]:
        return self.service.get_all_contents(self.session)

    def update_content(self, content_id: int, content_data: dict) -> Content:
        return self.service.update_content(self.session, content_id, content_data)

    def delete_content(self, content_id: int) -> None:
        self.service.delete_content(self.session, content_id)
