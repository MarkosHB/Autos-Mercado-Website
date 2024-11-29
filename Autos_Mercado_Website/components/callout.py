import reflex as rx


# TODO.
def callout() -> rx.Component:
    return rx.flex(
        rx.callout(
            "You will need admin privileges to install and access this application.",
            icon="info",
            color_scheme="blue",
        ),
        rx.callout(
            "You will need admin privileges to install and access this application.",
            icon="info",
            color_scheme="green",
        ),
        rx.callout(
            "You will need admin privileges to install and access this application.",
            icon="triangle_alert",
            role="alert",
            color_scheme="red",
        ),
        direction="column",
        spacing="3",
    )