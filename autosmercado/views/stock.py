import reflex as rx

from autosmercado.components.car_preview import car_preview
from autosmercado.styles.styles import Spacing, Size
from autosmercado.supabase.PageState import PageState


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
                                    rx.text(
                                        "Cargando...",
                                        height="250px",
                                    ),
                                    side="top",
                                    pb="current",
                                    clip="padding-box",
                                ),
                                rx.heading(
                                    "Estamos obteniendo la información del vehículo"
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
                        lambda coche: car_preview(coche),
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
