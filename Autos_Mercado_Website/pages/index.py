import reflex as rx

from Autos_Mercado_Website.routes import Route
import Autos_Mercado_Website.utils as utils
from Autos_Mercado_Website.components.status_chip import status_chip
from Autos_Mercado_Website.components.dark_mode_toggle import dark_mode_toggle
from Autos_Mercado_Website.components.car_preview import car_preview

from Autos_Mercado_Website.styles.styles import Spacing

from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.footer import footer

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
                rx.box(
                    dark_mode_toggle(),
                    width="100%",
                    margin="12px",
                    padding="12px",
                ),
                rx.image(
                    src="/fachada.jpg",
                    border_radius="25px 25px",
                    border="4px solid #0a0e12",
                ),
                rx.hstack(
                    status_chip("Info", "info", "blue"),
                    status_chip("Success", "circle-check", "green"),
                    status_chip("Warning", "circle-alert", "yellow"),
                    status_chip("Error", "circle-x", "red"),
                    wrap="wrap",
                    spacing="2",
                ),
                car_preview(),
                # stock(),
                footer(),
                spacing=Spacing.VERY_BIG.value,
                align="center",
                width="100%"
            )
        )
    )
