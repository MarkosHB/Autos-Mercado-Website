import reflex as rx

from Autos_Mercado_Website.components.car_preview import car_preview
from Autos_Mercado_Website.styles.styles import Spacing, Size
from Autos_Mercado_Website.supabase.PageState import PageState


def stock() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.grid(
                rx.foreach(
                    PageState.vehiculo_info,
                    lambda coche, index: car_preview(coche, index),
                ),
                gap="2rem",
                grid_template_columns=[
                    "1fr",
                    "repeat(2, 1fr)",
                    "repeat(2, 1fr)",
                    "repeat(3, 1fr)",
                    "repeat(4, 1fr)",
                ],
                width="100%",
                spacing=Spacing.DEFAULT.value,
            ),
            width="100%",
            justify="center",
            padding=Size.BIG.value,
            flex_wrap="wrap",

        ),
        on_mount=PageState.get_data
    )
