import reflex as rx

from autosmercado.routes import Route
import autosmercado.utils as utils

from autosmercado.styles.styles import Spacing
from autosmercado.components.form import mobile_form

from autosmercado.views.header import header
from autosmercado.views.navbar import navbar
from autosmercado.views.footer import footer

import autosmercado.texts as texto

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
