import reflex as rx

from Autos_Mercado_Website.components.car_preview import car_preview
from Autos_Mercado_Website.styles.styles import Spacing, Size


def stock() -> rx.Component:
    return rx.flex(
        rx.grid(
            rx.foreach(
                rx.Var.range(12),
                lambda idx: car_preview(idx, "Modelo"),
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
    )

