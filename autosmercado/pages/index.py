import reflex as rx

from autosmercado.routes import Route
import autosmercado.utils as utils

from autosmercado.components.dark_mode_toggle import dark_mode_toggle
from autosmercado.styles.styles import Spacing, Size
import autosmercado.texts as texto
from autosmercado.supabase.PageState import PageState

from autosmercado.views.navbar import navbar
from autosmercado.views.footer import footer
from autosmercado.views.stock import stock
from autosmercado.views.welcome import welcome

ROUTE = Route.INDEX


@rx.page(
    title=utils.title_index,
    on_load=PageState.get_data
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
