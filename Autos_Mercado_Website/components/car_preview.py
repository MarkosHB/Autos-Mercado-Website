import reflex as rx

from Autos_Mercado_Website.styles.styles import Spacing
from Autos_Mercado_Website.supabase.vehiculo import Vehiculo


# TODO rx.skeleton()
def car_preview(vehiculo: Vehiculo) -> rx.Component:
    return rx.link(
        rx.card(
            rx.inset(
                rx.image(
                    src="/lo" + "go.png",
                    width="100%",
                    height="auto",
                ),
                side="top",
                pb="current",
                clip="padding-box",
            ),
            rx.heading(
                vehiculo.modelo
            ),
            width="100%",
            spacing=Spacing.DEFAULT.value,
        ),
        href="",
    )
