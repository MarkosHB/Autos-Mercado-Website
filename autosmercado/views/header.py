import reflex as rx
from autosmercado.components.heading import heading
from autosmercado.components.dark_mode_toggle import dark_mode_toggle
from autosmercado.components.badge_chip import badge_chip


def header(pagina: str, titulo: str, text1: str, text2: str) -> rx.Component:
    return rx.box(
        badge_chip("Novedosa opción exclusiva", "violet") if pagina == "COCHES_A_LA_CARTA" else rx.fragment(),
        badge_chip("No dude en preguntarnos", "brown") if pagina == "VENDEMOS_SU_VEHICULO" else rx.fragment(),
        badge_chip("Esperamos su visita", "pink") if pagina == "SOBRE_NOSOTROS" else rx.fragment(),
        badge_chip("Escríbanos con confianza", "red") if pagina == "CONTACTO" else rx.fragment(),
        rx.box(
            dark_mode_toggle(),
            position="absolute",
            top="12px",
            right="24px",
        ),
        rx.container(
            rx.card(
                heading(
                    pagina,
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
