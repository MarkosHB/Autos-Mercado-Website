import reflex as rx

import autosmercado.utils as utils
from autosmercado.routes import Route

from autosmercado.styles.styles import Spacing

from autosmercado.views.navbar import navbar
from autosmercado.views.header import header
from autosmercado.views.pasos_a_la_carta import pasos_a_la_carta
from autosmercado.views.footer import footer

import autosmercado.texts as texto

ROUTE = Route.COCHESALACARTA


@rx.page(
    title=utils.title_cochesalacarta,
    route=ROUTE.value,
)
def cochesalacarta() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    pagina="COCHES_A_LA_CARTA",
                    titulo=texto.COCHES_A_LA_CARTA_TITULO,
                    text1=texto.COCHES_A_LA_CARTA_TEXTO1,
                    text2=texto.COCHES_A_LA_CARTA_TEXTO2,
                ),
                pasos_a_la_carta(
                    header1=texto.DESPLEGABLE_HEADER1,
                    header2=texto.DESPLEGABLE_HEADER2,
                    header3=texto.DESPLEGABLE_HEADER3,
                    texto1=texto.DESPLEGABLE_TEXTO1,
                    texto2=texto.DESPLEGABLE_TEXTO2,
                    texto3=texto.DESPLEGABLE_TEXTO3,
                ),
                footer(),
                spacing=Spacing.DEFAULT.value,
                align="center",
                width="100%"
            )
        )
    )
