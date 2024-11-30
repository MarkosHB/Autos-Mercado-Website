import reflex as rx

from Autos_Mercado_Website.components.accordion import accordion
from Autos_Mercado_Website.styles.styles import Size


def pasos_a_la_carta(header1: str, header2: str, header3: str,
                     texto1: str, texto2: str, texto3: str) -> rx.Component:
    return rx.container(
        accordion(
            header1,
            header2,
            header3,
            texto1,
            texto2,
            texto3,
        ),
    )
