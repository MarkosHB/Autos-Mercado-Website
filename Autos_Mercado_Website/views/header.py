import reflex as rx
from Autos_Mercado_Website.components.heading import heading
from Autos_Mercado_Website.styles.styles import Spacing
from Autos_Mercado_Website.views.mode_switch import dark_mode_toggle


def header(titulo: str, text1: str, text2: str) -> rx.Component:
    return rx.box(
        dark_mode_toggle(),
        rx.container(
            rx.card(
                heading(
                    titulo,
                    text1,
                    text2,
                ),
                width="100%",
                variant="ghost"
            ),
            size="4",
        ),
        width="100%",
        margin="12px",
        padding="12px",
    )
