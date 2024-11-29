import reflex as rx

from Autos_Mercado_Website.styles.styles import Color


def welcome() -> rx.Component:
    return rx.center(
        rx.image(
            src="/interior.jpg",
            border_radius="25px 25px",
            border="2px solid white",
        ),
        width="100%",
        padding="32px",
        background=Color.SECONDARY.value
    )
