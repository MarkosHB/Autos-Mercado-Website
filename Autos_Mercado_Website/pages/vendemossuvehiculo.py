import reflex as rx

import Autos_Mercado_Website.utils as utils
from Autos_Mercado_Website.routes import Route

from Autos_Mercado_Website.styles.styles import Spacing

from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.header import header
from Autos_Mercado_Website.views.footer import footer

import Autos_Mercado_Website.texts as texto

ROUTE = Route.VENDEMOSSUVEHICULO


@rx.page(
    title=utils.title_vendemossuvehiculo,
    route=ROUTE.value,
)
def vendemossuvehiculo() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    pagina="VENDEMOS_SU_VEHICULO",
                    titulo=texto.VENDEMOS_SU_VEHICULO_TITULO,
                    text1=texto.VENDEMOS_SU_VEHICULO_TEXTO1,
                    text2=texto.VENDEMOS_SU_VEHICULO_TEXTO2,
                ),
                rx.center(
                    rx.image(
                        src="/antigua_fachada.png",
                        border_radius="20px 20px",
                        border="1px solid gray",

                    ),
                    width="100%",
                    padding="0px 32px 32px 32px",
                ),
                footer(),
                spacing=Spacing.DEFAULT.value,
                align="center",
                width="100%"
            )
        )
    )
