import reflex as rx

from Autos_Mercado_Website.components.rectangle_content import rectangle_content
from Autos_Mercado_Website.styles.styles import Size


def heading(titulo: str, texto1="", texto2="") -> rx.Component:
    return rx.vstack(
        rx.blockquote(titulo, weight="bold", size="8", color_scheme="blue"),

        rx.tablet_and_desktop(
            rx.hstack(
                rectangle_content(texto1),
                rectangle_content(texto2),
                gap=Size.BIG.value,
            ),
        ),
        rx.mobile_only(
            rx.vstack(
                rectangle_content(texto1),
                rectangle_content(texto2),
                gap=Size.VERY_SMALL.value,
            )
        ),
        width="100%",
    )
