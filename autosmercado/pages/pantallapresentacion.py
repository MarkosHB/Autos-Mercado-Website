import reflex as rx
from autosmercado.routes import Route
import autosmercado.utils as utils
from autosmercado.supabase.PresentationState import PresentationState

ROUTE = Route.PANTALLAPRESENTACION

@rx.page(
    title=utils.title_pantallapresentacion,
    route=ROUTE.value,
    on_load=PresentationState.on_load,
)
def pantallapresentacion() -> rx.Component:
    return rx.box(
        utils.lang(),
        rx.center(
            rx.vstack(
                rx.image(
                    src=PresentationState.fotos_presentacion[PresentationState.current_image_idx], 
                    width="100%", height="100%", object_fit="contain",
                ),
                rx.moment(
                    interval=PresentationState.interval,
                    on_change=PresentationState.cambiar_imagen,
                    format="HH:mm:ss",
                    display="none",
                ),
                width="100vw",
                height="100vh",
            ),
            width="100vw",
            height="100vh",
        ),
        width="100vw",
        height="100vh",
    )
