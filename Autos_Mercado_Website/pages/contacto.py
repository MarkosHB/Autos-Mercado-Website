import reflex as rx

from Autos_Mercado_Website.routes import Route
import Autos_Mercado_Website.utils as utils

from Autos_Mercado_Website.styles.styles import Spacing
from Autos_Mercado_Website.components.form import mobile_form
from Autos_Mercado_Website.views.header import header

from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.footer import footer

import Autos_Mercado_Website.texts as texto

ROUTE = Route.CONTACTO


@rx.page(
    title=utils.title_contacto
)
def contacto() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    pagina="CONTACTO",
                    titulo=texto.CONTACTO_TITULO,
                    text1=texto.CONTACTO_TEXTO1,
                    text2="",
                ),
                rx.container(
                    mobile_form(),
                    size="4",
                ),
                footer(),
                spacing=Spacing.DEFAULT_BIG.value,
                align="center",
                width="100%"
            )
        )
    )
