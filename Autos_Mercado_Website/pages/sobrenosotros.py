import reflex as rx

import Autos_Mercado_Website.utils as utils
from Autos_Mercado_Website.routes import Route

import Autos_Mercado_Website.texts as texto
import Autos_Mercado_Website.constants as const
from Autos_Mercado_Website.styles.styles import Spacing

from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.header import header
from Autos_Mercado_Website.views.footer import footer

from Autos_Mercado_Website.components.data_list import data_list

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
                rx.vstack(
                    rx.callout(
                        rx.text(
                            const.DIRECCION,
                            size="4",
                        ),
                        size="3",
                        icon="Map-pin",
                        variant="soft",
                        color_scheme="blue",
                    ),
                    rx.image(
                        src="/interior.jpg",
                        border_radius="20px 20px",
                        border="1px solid gray",
                    ),
                    rx.flex(
                        data_list(),
                        data_list(),
                        wrap="wrap",
                    ),
                    width="100%",
                    align="center",
                    spacing=Spacing.BIG.value,
                    padding="0px 32px 32px 32px",
                ),
                footer(),
                spacing=Spacing.DEFAULT.value,
                align="center",
                width="100%"
            )
        )
    )
