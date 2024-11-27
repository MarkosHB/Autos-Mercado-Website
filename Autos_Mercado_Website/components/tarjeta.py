import reflex as rx
from Autos_Mercado_Website.styles.colors import TextColor


def tarjeta(icono: str, color: TextColor, link: str, texto: str) -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.icon(icono, size=20, color=color),
                rx.text(texto, size="2", weight="bold"),
                spacing="2",
            ),
            href=link
        ),
        as_child=True,
    )