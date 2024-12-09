import reflex as rx

from Autos_Mercado_Website.components.data_list import data_list
from Autos_Mercado_Website.supabase.PageState import PageState
from Autos_Mercado_Website.components.dark_mode_toggle import dark_mode_toggle
from Autos_Mercado_Website.styles.styles import Spacing, Size


def car_display() -> rx.Component:
    return rx.cond(
        # https://reflex.dev/docs/library/dynamic-rendering/cond/
        PageState.car_loading,

        # Si aún no se ha cargado, mostrar una plantilla oculta (skeleton).
        rx.skeleton(rx.text("Prueba")),

        # Una vez cargado, mostrar los detalles del vehiculo.

        rx.vstack(
            dark_mode_toggle(),
            rx.blockquote(PageState.vehiculo_info.modelo, weight="bold", size="8", color_scheme="blue"),
            rx.container(
                rx.desktop_only(
                    rx.hstack(
                        rx.image(
                            src=PageState.image,
                            border_radius="20px 20px",
                            border="1px solid gray",
                            width="60%"
                        ),
                        rx.vstack(
                            rx.heading(
                                f"{PageState.vehiculo_info.precio_venta} €",
                                weight="bold",
                                size="9",
                            ),
                            rx.heading(
                                f"Financiado por {PageState.vehiculo_info.precio_financiado} €/mes",
                                weight="medium",
                                size="5",
                            ),
                            data_list(
                                v1=PageState.vehiculo_info.anio,
                                v2=PageState.vehiculo_info.tipo,
                                v3=PageState.vehiculo_info.combustible,
                                v4=PageState.vehiculo_info.transmision,
                                v5=PageState.vehiculo_info.kilometraje,
                                v6=PageState.vehiculo_info.caballos,
                                v7=PageState.vehiculo_info.cilindrada,
                                v8=PageState.vehiculo_info.puertas,
                                v9=PageState.vehiculo_info.color,
                            ),
                        ),
                        align="center",
                        width="100%",
                        gap=Size.VERY_BIG.value,
                    ),
                ),

                rx.mobile_and_tablet(
                    rx.vstack(
                        rx.image(
                            src=PageState.image,
                            border_radius="20px 20px",
                            border="1px solid gray",
                            width="100%"
                        ),
                        rx.vstack(
                            rx.heading(
                                f"{PageState.vehiculo_info.precio_venta} €",
                                weight="bold",
                                size="9",
                            ),
                            rx.heading(
                                f"Financiado por {PageState.vehiculo_info.precio_financiado} €/mes",
                                weight="medium",
                                size="5",
                            ),
                        ),
                        data_list(
                            v1=PageState.vehiculo_info.anio,
                            v2=PageState.vehiculo_info.tipo,
                            v3=PageState.vehiculo_info.combustible,
                            v4=PageState.vehiculo_info.transmision,
                            v5=PageState.vehiculo_info.kilometraje,
                            v6=PageState.vehiculo_info.caballos,
                            v7=PageState.vehiculo_info.cilindrada,
                            v8=PageState.vehiculo_info.puertas,
                            v9=PageState.vehiculo_info.color,
                        ),
                        align="center",
                        width="100%",
                        gap=Size.VERY_BIG.value,
                    ),
                ),
                size="4",
            ),
            align="center",
            margin="12px",
            width="100%",
            spacing=Spacing.BIG.value,
            padding=Size.DEFAULT.value,
        ),
    )
