import reflex as rx

from Autos_Mercado_Website.styles.styles import Spacing
from Autos_Mercado_Website.supabase.PageState import PageState
from Autos_Mercado_Website.supabase.vehiculo import Vehiculo


def car_preview(vehiculo: Vehiculo, idx: int) -> rx.Component:
    return rx.link(
        rx.card(
            rx.inset(
                rx.image(
                    src=PageState.preview_images[idx],
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
            rx.text(
                vehiculo.precio_venta
            ),
            rx.text(
                vehiculo.precio_financiado
            ),
            width="100%",
            spacing=Spacing.DEFAULT.value,
        ),
        href=f"/detalles-del-vehiculo/{vehiculo.url_modelo}",
    )
