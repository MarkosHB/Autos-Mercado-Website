import reflex as rx
from Autos_Mercado_Website.styles.colors import Color, TextColor


def social_link(icono: str, color: TextColor, link: str, texto: str) -> rx.Component:
    return rx.button(
        rx.link(
            rx.flex(
                rx.icon(icono, size=20, color=color),
                rx.text(texto, size="2", weight="bold"),
                spacing="2",
            ),
            href=link
        ),
        as_child=True,
        radius="large",
        size="3",
        variant="surface",
        bg_color=Color.TERTIARY.value,
    )
