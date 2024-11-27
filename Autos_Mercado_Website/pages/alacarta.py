import reflex as rx

from Autos_Mercado_Website.routes import Route
import Autos_Mercado_Website.utils as utils


ROUTE = Route.ALACARTA


@rx.page(
    title=utils.title_alacarta
)
def alacarta() -> rx.Component:
    return