import reflex as rx
from apps.content.presentation.state import ContentState
from apps.content.presentation.components import content_card, content_form


def content_list_page() -> rx.Component:
    ContentState.load_contents()  # Load contents when the page is accessed
    return rx.box(
        rx.heading("Contents", size="2xl"),
        rx.link(rx.button("Add New Content"), href="/contents/create"),
        rx.foreach(
            lambda: ContentState.content_list,
            lambda content: content_card(
                content.get("title", ""),
                content.get("author", ""),
                content.get("content_type", ""),
                content.get("link", ""),
                content.get("id", 0),
            ),
        ),
        padding="6",
        margin="6",
    )


def content_create_page() -> rx.Component:
    return rx.box(
        rx.heading("Create Content", size="2xl"),
        content_form("/contents/create"),
        padding="6",
        margin="6",
    )


def content_detail_page(content_id: int) -> rx.Component:
    content = ContentState.get_content(content_id)
    return rx.box(
        rx.heading(content.get("title", ""), size="2xl"),
        rx.text(f"Author: {content.get('author', '')}"),
        rx.text(f"Type: {content.get('content_type', '')}"),
        rx.link(
            f"Link: {content.get('link', '')}",
            href=content.get("link", ""),
            is_external=True,
        ),
        rx.text(content.get("content", "")),
        rx.link(rx.button("Edit"), href=f"/contents/{content_id}/update"),
        rx.button("Delete", on_click=lambda: ContentState.delete_content(content_id)),
        padding="6",
        margin="6",
    )


def content_update_page(content_id: int) -> rx.Component:
    content = ContentState.get_content(content_id)
    return rx.box(
        rx.heading("Update Content", size="2xl"),
        content_form(f"/contents/{content_id}/update", content_data=content),
        padding="6",
        margin="6",
    )
