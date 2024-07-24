"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from apps.content.presentation.pages import (
    content_create_page,
    content_list_page,
    content_update_page,
    content_detail_page,
)


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
app.add_page(content_list_page, route="/contents")
app.add_page(content_create_page, route="/contents/create")
app.add_page(content_detail_page, route="/contents/<int:content_id>")
app.add_page(content_update_page, route="/contents/<int:content_id>/update")
