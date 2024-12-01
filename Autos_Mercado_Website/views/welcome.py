import reflex as rx

from Autos_Mercado_Website.styles.styles import Color


def welcome() -> rx.Component:
    return rx.center(
        rx.image(
            src="/fachada.jpg",
            border_radius="20px 20px",
            border="2px solid white",
        ),
        width="100%",
        padding="32px",
        background=Color.SECONDARY.value
    )
