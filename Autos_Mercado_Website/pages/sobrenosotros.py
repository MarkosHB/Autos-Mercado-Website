import reflex as rx

import Autos_Mercado_Website.utils as utils
from Autos_Mercado_Website.routes import Route
from Autos_Mercado_Website.styles.colors import Color


from Autos_Mercado_Website.styles.styles import Spacing

from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.header import header
from Autos_Mercado_Website.views.footer import footer

from Autos_Mercado_Website.components.data_list import data_list
import Autos_Mercado_Website.texts as texto

ROUTE = Route.SOBRENOSOTROS


@rx.page(
    title=utils.title_sobrenosotros,
    route=ROUTE.value,
)
def sobrenosotros() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    pagina="SOBRE_NOSOTROS",
                    titulo=texto.SOBRE_NOSOTROS_TITULO,
                    text1=texto.SOBRE_NOSOTROS_TEXTO1,
                    text2=texto.SOBRE_NOSOTROS_TEXTO2,
                ),
                data_list(),
                rx.center(
                    rx.image(
                        src="/fachada.jpg",
                        border_radius="25px 25px",
                        border="2px solid white",
                    ),
                    width="100%",
                    padding="32px",
                    background=Color.SECONDARY.value
                ),
                footer(),
                spacing=Spacing.DEFAULT_BIG.value,
                align="center",
                width="100%"
            )
        )
    )
