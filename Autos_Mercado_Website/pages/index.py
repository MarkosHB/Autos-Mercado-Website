import reflex as rx

from Autos_Mercado_Website.routes import Route
import Autos_Mercado_Website.utils as utils

from Autos_Mercado_Website.components.dark_mode_toggle import dark_mode_toggle
from Autos_Mercado_Website.styles.styles import Spacing, Size
import Autos_Mercado_Website.texts as texto

from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.footer import footer
from Autos_Mercado_Website.views.stock import stock
from Autos_Mercado_Website.views.welcome import welcome

ROUTE = Route.INDEX


@rx.page(
    title=utils.title_index
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                welcome(),
                rx.vstack(
                    dark_mode_toggle(),
                    rx.spacer(),
                    rx.blockquote(texto.CATALOGO_TITULO, weight="bold", size="8", color_scheme="blue"),
                    align="center",
                    width="100%",
                    spacing=Spacing.DEFAULT.value,
                    padding=Size.DEFAULT.value,
                ),
                stock(),
                footer(),
                spacing=Spacing.DEFAULT_BIG.value,
                align="center",
                width="100%",
            )
        )
    )
