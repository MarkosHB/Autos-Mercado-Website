import reflex as rx

import Autos_Mercado_Website.utils as utils
from Autos_Mercado_Website.routes import Route

from Autos_Mercado_Website.styles.styles import Spacing

from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.header import header
from Autos_Mercado_Website.views.stock import stock
from Autos_Mercado_Website.views.footer import footer


ROUTE = Route.SOBRENOSOTROS


@rx.page(
    title=utils.title_sobrenosotros
)
def compramostucoche() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(),
                # stock(),
                footer(),
                spacing=Spacing.VERY_BIG.value,
                align="center",
                width="100%"
            )
        )
    )