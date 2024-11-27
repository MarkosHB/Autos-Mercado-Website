import reflex as rx

from Autos_Mercado_Website.routes import Route
import Autos_Mercado_Website.utils as utils


ROUTE = Route.SOBRENOSOTROS


@rx.page(
    title=utils.title_sobrenosotros
)
def sobrenosotros() -> rx.Component:
    return