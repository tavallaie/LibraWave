import reflex as rx


def content_card(
    title: str, author: str, content_type: str, link: str, content_id: int
) -> rx.Component:
    return rx.box(
        rx.heading(title, size="md"),
        rx.text(f"Author: {author}"),
        rx.text(f"Type: {content_type}"),
        rx.link(f"Link: {link}", href=link, is_external=True),
        rx.button("Read More", href=f"/contents/{content_id}"),
        padding="4",
        border="1px solid",
        border_radius="md",
        box_shadow="md",
        margin="4",
    )
