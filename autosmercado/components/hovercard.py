import reflex as rx


# TODO. pensar donde poner
def hovercard() -> rx.Component:
    return rx.text(
        "Hover over the text to see the tooltip. ",
        rx.hover_card.root(
            rx.hover_card.trigger(
                rx.link(
                    "Hover over me",
                    color_scheme="blue",
                    underline="always",
                ),
            ),
            rx.hover_card.content(
                rx.text("This is the hovercard content."),
            ),
        ),
    )

