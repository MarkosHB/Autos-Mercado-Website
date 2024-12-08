import reflex as rx

from Autos_Mercado_Website.routes import Route
import Autos_Mercado_Website.utils as utils
from Autos_Mercado_Website.styles.styles import Spacing
from Autos_Mercado_Website.supabase.PageState import PageState
from Autos_Mercado_Website.supabase.vehiculo import Vehiculo

from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.footer import footer


ROUTE = Route.DETALLESVEHICULO


@rx.page(
    title=utils.title_detallesvehiculo,
    route=ROUTE.value,
)
def detallesvehiculo() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                rx.heading(f"Detalles del Vehículo: {PageState.vehiculo_info.modelo}"),
                footer(),
                spacing=Spacing.DEFAULT_BIG.value,
                align="center",
                width="100%",
                on_mount=PageState.get_car,
            )
        )
    )
