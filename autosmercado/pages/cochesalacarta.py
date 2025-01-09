import reflex as rx

import autosmercado.texts as texto
import autosmercado.utils as utils
from autosmercado.routes import Route

from autosmercado.styles.styles import Spacing
from autosmercado.components.accordion import accordion

from autosmercado.views.navbar import navbar
from autosmercado.views.header import header
from autosmercado.views.footer import footer

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
                rx.container(
                    accordion(
                        texto.DESPLEGABLE_HEADER1,
                        texto.DESPLEGABLE_HEADER2,
                        texto.DESPLEGABLE_HEADER3,
                        texto.DESPLEGABLE_TEXTO1,
                        texto.DESPLEGABLE_TEXTO2,
                        texto.DESPLEGABLE_TEXTO3,
                    ),
                    width="100%",
                ),
                footer(),
                spacing=Spacing.DEFAULT.value,
                align="center",
                width="100%"
            )
        )
    )
