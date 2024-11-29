import reflex as rx
from Autos_Mercado_Website.components.heading import heading
from Autos_Mercado_Website.components.dark_mode_toggle import dark_mode_toggle
from Autos_Mercado_Website.components.badge_chip import badge_chip
from Autos_Mercado_Website.styles.styles import Spacing


def header(pagina: str, titulo: str, text1: str, text2: str) -> rx.Component:
    return rx.box(
        badge_chip("Escríbenos con confianza", "green") if pagina == "COMPRAMOS_TU_COCHE" else rx.fragment(),
        badge_chip("Novedosa opción disponible", "violet") if pagina == "COCHES_A_LA_CARTA" else rx.fragment(),
        badge_chip("No dudes en contactarnos", "amber") if pagina == "SOBRE_NOSOTROS" else rx.fragment(),
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
                variant="classic",
                padding="24px",
            ),
            size="4",
        ),
        position="relative",
        width="100%",
        margin="12px",
        padding="12px",
    )
