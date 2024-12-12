import reflex as rx

import autosmercado.utils as utils
from autosmercado.routes import Route

import autosmercado.texts as texto
import autosmercado.constants as const
from autosmercado.styles.styles import Spacing

from autosmercado.views.navbar import navbar
from autosmercado.views.header import header
from autosmercado.views.footer import footer


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
