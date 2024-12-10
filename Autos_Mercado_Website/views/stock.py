import reflex as rx

from Autos_Mercado_Website.components.car_preview import car_preview
from Autos_Mercado_Website.styles.styles import Spacing, Size
from Autos_Mercado_Website.supabase.PageState import PageState


def stock() -> rx.Component:
    return rx.cond(
        # https://reflex.dev/docs/library/dynamic-rendering/cond/
        PageState.loading,

        # Si aún no se ha cargado, mostrar una plantilla oculta (skeleton).
        rx.vstack(
            rx.flex(
                rx.grid(
                    rx.foreach(
                        rx.Var.range(12),
                        lambda i: rx.skeleton(
                            rx.card(
                                rx.inset(
                                    rx.image(
                                        src="logo.png",
                                        width="100%",
                                        height="auto",
                                    ),
                                    side="top",
                                    pb="current",
                                    clip="padding-box",
                                ),
                                rx.heading(
                                    "Esto es un texto de prueba lo suficientemente largo ..."
                                ),
                                width="100%",
                                spacing=Spacing.DEFAULT.value,
                            ),
                            loading=True,
                        ),
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
        ),

        # Una vez cargado, mostrar el listado de vehiculos en Stock.
        rx.vstack(
            rx.flex(
                rx.grid(
                    rx.foreach(
                        PageState.vehiculos_info,
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
        ),
    )
