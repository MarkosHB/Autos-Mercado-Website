import reflex as rx

from autosmercado.styles.styles import Spacing
from autosmercado.supabase.PageState import PageState
from autosmercado.supabase.vehiculo import Vehiculo


def car_preview(vehiculo: Vehiculo, idx: int) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=vehiculo.imagen_public_url,
                    width="100%",
                    height="auto",
                ),
                side="top",
                pb="current",
                clip="padding-box",
            ),
            href=f"/detalles-del-vehiculo/{vehiculo.url_modelo}",
        ),
        rx.vstack(
            rx.link(
                rx.heading(
                    vehiculo.modelo
                ),
                href=f"/detalles-del-vehiculo/{vehiculo.url_modelo}",
            ),
            rx.separator(),
            rx.spacer(),
            rx.text(
                f"{vehiculo.precio_venta} €",
                weight="bold",
                align="right",
                size="5",
            ),
            rx.text(
                f"Financiado por {vehiculo.precio_financiado} €/mes",
                align="center",
                weight="medium",
                size="3",
            ),

        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )
