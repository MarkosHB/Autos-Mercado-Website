import reflex as rx

import Autos_Mercado_Website.utils as utils
from Autos_Mercado_Website.components.form import form
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
                rx.center(
                    rx.image(
                        src="/interior.jpg",
                        border_radius="20px 20px",
                        border="1px solid gray",

                    ),
                    width="100%",
                    padding="0px 32px 32px 32px",
                ),
                #data_list(),
                #TODO
                # social_link("Map-pin", TextColor.YELLOW, None, const.DIRECCION),
                form(),
                footer(),
                spacing=Spacing.DEFAULT.value,
                align="center",
                width="100%"
            )
        )
    )
