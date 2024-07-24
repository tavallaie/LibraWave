import reflex as rx


def content_form(action: str, content_data: dict = None) -> rx.Component:
    content_data = content_data or {}
    return rx.form(
        rx.input(
            name="title", placeholder="Title", value=content_data.get("title", "")
        ),
        rx.input(
            name="author", placeholder="Author", value=content_data.get("author", "")
        ),
        rx.input(
            name="content_type",
            placeholder="Content Type",
            value=content_data.get("content_type", ""),
        ),
        rx.input(name="link", placeholder="Link", value=content_data.get("link", "")),
        rx.text_area(
            name="content", placeholder="Content", value=content_data.get("content", "")
        ),
        rx.button(action, type="submit"),
        method="post",
        action=action,
    )
