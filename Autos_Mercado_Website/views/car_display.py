import reflex as rx

from Autos_Mercado_Website.components.data_list import data_list
from Autos_Mercado_Website.components.title import title
from Autos_Mercado_Website.supabase.DisplayState import DisplayState
from Autos_Mercado_Website.components.dark_mode_toggle import dark_mode_toggle
from Autos_Mercado_Website.styles.styles import Spacing, Size


def car_display() -> rx.Component:
    return rx.cond(
        # https://reflex.dev/docs/library/dynamic-rendering/cond/
        DisplayState.car_loading,

        # Si aún no se ha cargado, mostrar una plantilla oculta (skeleton).
        rx.vstack(
            dark_mode_toggle(),
            rx.center(
                rx.hstack(
                    rx.skeleton(
                        width="100px",
                        height="100px",
                        background_color="blue",
                        margin="10px"
                    ),
                    rx.skeleton(
                        width="100px",
                        height="100px",
                        background_color="red",
                        margin="10px"
                    )
                )
            ),
            align="center",
            margin="12px",
            width="100%",
            spacing=Spacing.BIG.value,
            padding=Size.DEFAULT.value,
        ),

        # Una vez cargado, mostrar los detalles del vehiculo.
        rx.vstack(
            dark_mode_toggle(),
            rx.blockquote(DisplayState.vehiculo_info.modelo, weight="bold", size="8", color_scheme="blue"),
            rx.container(

                rx.desktop_only(

                    rx.hstack(
                        rx.image(
                            src=DisplayState.image,
                            border_radius="20px 20px",
                            border="1px solid gray",
                            width="60%"
                        ),

                        rx.vstack(
                            rx.heading(
                                f"{DisplayState.vehiculo_info.precio_venta} €", weight="bold", size="9",
                            ),
                            rx.heading(
                                f"Financiado por {DisplayState.vehiculo_info.precio_financiado} €/mes",
                                weight="medium", size="5",
                            ),
                            data_list(
                                v1=DisplayState.vehiculo_info.anio,
                                v2=DisplayState.vehiculo_info.tipo,
                                v3=DisplayState.vehiculo_info.combustible,
                                v4=DisplayState.vehiculo_info.transmision,
                                v5=DisplayState.vehiculo_info.kilometraje,
                                v6=DisplayState.vehiculo_info.caballos,
                                v7=DisplayState.vehiculo_info.cilindrada,
                                v8=DisplayState.vehiculo_info.puertas,
                                v9=DisplayState.vehiculo_info.color,
                            ),
                        ),
                        align="center",
                        width="100%",
                        gap=Size.VERY_BIG.value,
                    ),

                    rx.box(botones_cochesnet_milanuncios(), margin="20px"),

                ),

                rx.mobile_and_tablet(

                    rx.vstack(
                        rx.image(
                            src=DisplayState.image,
                            border_radius="20px 20px",
                            border="1px solid gray",
                            width="100%"
                        ),

                        rx.vstack(
                            rx.heading(f"{DisplayState.vehiculo_info.precio_venta} €", weight="bold", size="9"),
                            rx.heading(
                                f"Financiado por {DisplayState.vehiculo_info.precio_financiado} €/mes",
                                weight="medium", size="5",
                            ),
                        ),

                        data_list(
                            v1=DisplayState.vehiculo_info.anio,
                            v2=DisplayState.vehiculo_info.tipo,
                            v3=DisplayState.vehiculo_info.combustible,
                            v4=DisplayState.vehiculo_info.transmision,
                            v5=DisplayState.vehiculo_info.kilometraje,
                            v6=DisplayState.vehiculo_info.caballos,
                            v7=DisplayState.vehiculo_info.cilindrada,
                            v8=DisplayState.vehiculo_info.puertas,
                            v9=DisplayState.vehiculo_info.color,
                        ),

                        botones_cochesnet_milanuncios(),

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


def botones_cochesnet_milanuncios() -> rx.Component:
    return rx.flex(
        rx.cond(
            DisplayState.vehiculo_info.coches_punto_net == "N/A",
            rx.fragment(),
            rx.button(
                rx.link(
                    title("Coches.net", size=[Size.DEFAULT_BIG.value]),
                    href=DisplayState.vehiculo_info.coches_punto_net
                ),
                radius="large",
                size="4",
                color_scheme="red",
                variant="classic"
            ),
        ),
        rx.cond(
            DisplayState.vehiculo_info.milanuncios == "N/A",
            rx.fragment(),
            rx.button(
                rx.link(
                    title("Milanuncios", size=[Size.DEFAULT_BIG.value]),
                    href=DisplayState.vehiculo_info.milanuncios
                ),
                radius="large",
                size="4",
                color_scheme="jade",
                variant="classic"
            )
        ),
        gap=Size.DEFAULT.value,
        align="center",
        wrap="wrap",
    )
