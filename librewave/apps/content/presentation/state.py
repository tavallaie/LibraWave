import reflex as rx
from apps.content.application.content_manager import ContentManager

content_manager = ContentManager()


class ContentState(rx.State):
    content_list: list[dict] = []
    content: dict = {}

    @rx.var
    def all_contents(self) -> list[dict]:
        return self.content_list

    def load_contents(self):
        contents = content_manager.get_all_contents()
        self.content_list = [content.dict() for content in contents]

    def get_content(self, content_id: int) -> dict:
        content = content_manager.get_content(content_id)
        self.content = content.dict()
        return self.content

    def create_content(self, data: dict):
        content_manager.create_content(data)
        self.load_contents()

    def update_content(self, content_id: int, data: dict):
        content_manager.update_content(content_id, data)
        self.load_contents()

    def delete_content(self, content_id: int):
        content_manager.delete_content(content_id)
        self.load_contents()
