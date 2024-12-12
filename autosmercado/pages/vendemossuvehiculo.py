import reflex as rx

import autosmercado.utils as utils
from autosmercado.routes import Route

from autosmercado.styles.styles import Spacing

from autosmercado.views.navbar import navbar
from autosmercado.views.header import header
from autosmercado.views.footer import footer

import autosmercado.texts as texto

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
