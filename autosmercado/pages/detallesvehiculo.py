import reflex as rx

from autosmercado.routes import Route
import autosmercado.utils as utils
from autosmercado.styles.styles import Spacing
from autosmercado.supabase.DisplayState import DisplayState

from autosmercado.views.car_display import car_display
from autosmercado.views.navbar import navbar
from autosmercado.views.footer import footer


ROUTE = Route.DETALLESVEHICULO


@rx.page(
    title=utils.title_detallesvehiculo,
    route=ROUTE.value,
    on_load=DisplayState.get_car,
)
def detallesvehiculo() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                car_display(),
                footer(),
                spacing=Spacing.DEFAULT_BIG.value,
                align="center",
                width="100%",
            )
        )
    )
