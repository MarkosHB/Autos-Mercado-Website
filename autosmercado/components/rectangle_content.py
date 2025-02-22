import reflex as rx
from autosmercado.styles.styles import Size


def rectangle_content(texto: str) -> rx.Component:
    return rx.box(
        rx.text(
            texto,
            margin_top=Size.SMALL.value,
            size="5"
        ),
        padding=Size.MEDIUM.value,
    )
