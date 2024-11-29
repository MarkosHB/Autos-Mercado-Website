import reflex as rx
from Autos_Mercado_Website.components.heading import heading
from Autos_Mercado_Website.components.dark_mode_toggle import dark_mode_toggle


def header(titulo: str, text1: str, text2: str) -> rx.Component:
    return rx.box(
        rx.box(
            dark_mode_toggle(),
            position="absolute",
            top="12px",
            right="24px",
        ),
        rx.container(
            rx.card(
                heading(
                    titulo,
                    text1,
                    text2,
                ),
                margin_top="24px",
                width="100%",
                variant="ghost"
            ),
            size="4",
        ),
        position="relative",
        width="100%",
        margin="12px",
        padding="12px",
    )
