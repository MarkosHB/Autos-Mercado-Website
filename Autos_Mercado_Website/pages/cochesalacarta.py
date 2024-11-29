import reflex as rx

import Autos_Mercado_Website.utils as utils
from Autos_Mercado_Website.routes import Route

from Autos_Mercado_Website.styles.styles import Spacing

from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.header import header
from Autos_Mercado_Website.views.footer import footer

from Autos_Mercado_Website.components.accordion import accordion
import Autos_Mercado_Website.texts as texto

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
                accordion(),
                footer(),
                spacing=Spacing.VERY_BIG.value,
                align="center",
                width="100%"
            )
        )
    )