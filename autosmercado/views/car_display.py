import reflex as rx

from autosmercado.components.data_list import data_list
from autosmercado.components.title import title
from autosmercado.supabase.DisplayState import DisplayState
from autosmercado.components.dark_mode_toggle import dark_mode_toggle
from autosmercado.styles.styles import Spacing, Size


def car_display() -> rx.Component:
    return rx.cond(
        # https://reflex.dev/docs/library/dynamic-rendering/cond/
        DisplayState.car_loading,

        # Si aún no se ha cargado, mostrar una plantilla oculta (skeleton).
        skeleton(),

        # Una vez cargado, mostrar los detalles del vehiculo.
        rx.vstack(
            dark_mode_toggle(),
            rx.blockquote(DisplayState.vehiculo_info.modelo, weight="bold", size="8", color_scheme="blue"),
            detalles_vehiculo(),
            align="center",
            width="100%",
            spacing=Spacing.BIG.value,
            padding=Size.DEFAULT.value,
        ),
    )

def detalles_vehiculo() -> rx.Component:
    return rx.container(
        rx.desktop_only(
            rx.hstack(
                rx.vstack(
                    rx.hstack(
                        rx.icon("arrow-big-left", size=56, on_click=DisplayState.previous_image, stroke_width=1, color_scheme="gray"),
                        rx.image(
                            src=DisplayState.vehiculo_info.fotos[DisplayState.current_image_idx],
                            border_radius="20px 20px",
                            border="1px solid gray",
                            width="80%"
                        ),
                        rx.icon("arrow-big-right", size=56, on_click=DisplayState.next_image, stroke_width=1, color_scheme="gray"),
                        width="100%",
                        spacing=Spacing.DEFAULT.value,
                        padding=Size.DEFAULT.value,
                        align_items="center",
                        justify_content="center",
                    ),
                    pie_de_foto(),
                    align="center",
                    width="70%",
                    spacing=Spacing.SMALL.value,
                    padding=Size.DEFAULT.value,
                ),
                rx.vstack(
                    rx.heading(f"{DisplayState.vehiculo_info.precio_venta} €", weight="bold", size="9"),
                    rx.heading(f"Financiado por {DisplayState.vehiculo_info.precio_financiado} €/mes", weight="medium", size="5"),
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
                    align="center",
                    width="30%",
                    gap=Size.DEFAULT.value,
                    padding=Size.DEFAULT.value,
                ),
                align="center",
                width="100%",
                gap=Size.DEFAULT.value,
            ),    
        ),

        rx.mobile_and_tablet(
            rx.vstack(
                rx.vstack(
                    rx.image(
                        src=DisplayState.vehiculo_info.fotos[DisplayState.current_image_idx],
                        border_radius="20px 20px", border="1px solid gray", width="90%"
                    ),
                    rx.hstack(
                        rx.icon("arrow-big-left", size=36, on_click=DisplayState.previous_image, stroke_width=1, color_scheme="gray"),
                        rx.icon("arrow-big-right", size=36, on_click=DisplayState.next_image, stroke_width=1, color_scheme="gray"),
                        width="100%",
                        spacing=Spacing.SMALL.value,
                        padding=Size.SMALL.value,
                        align_items="center",
                        justify_content="center",
                    ),
                    width="100%",
                    spacing=Spacing.DEFAULT.value,
                    padding=Size.DEFAULT.value,
                    align_items="center",
                    justify_content="center",
                ),
                rx.vstack(
                    rx.heading(f"{DisplayState.vehiculo_info.precio_venta} €", weight="bold", size="9"),
                    rx.heading(f"Financiado por {DisplayState.vehiculo_info.precio_financiado} €/mes", weight="medium", size="5"),
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
                pie_de_foto(),
                align="center",
                width="100%",
                align_items="center",
                justify_content="center",
                gap=Size.BIG.value,
            ),
        ),
        size="4",
    )


def pie_de_foto() -> rx.Component:
    return rx.flex(
        rx.cond(
            DisplayState.vehiculo_info.coches_punto_net == "N/A",
            rx.fragment(),
            rx.button(
                rx.link(
                    title("Coches.net", size=[Size.DEFAULT_BIG.value]),
                    href=DisplayState.vehiculo_info.coches_punto_net
                ),
                radius="large", size="2", color_scheme="red", variant="solid"
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
                radius="large", size="2", color_scheme="jade", variant="solid"
            )
        ),
        rx.desktop_only(
            rx.hover_card.root(
                rx.hover_card.trigger(
                    rx.icon("qr-code", size=30, on_click=DisplayState.descargar_qr),
                ),
                rx.hover_card.content(
                    rx.text("Descargue el código QR"),
                    side="right", side_offset=15, align="center",
                ),
            )
        ),
        gap=Size.DEFAULT.value,
    )


def skeleton() -> rx.Component:
    return rx.vstack(
        dark_mode_toggle(),
        rx.skeleton(rx.heading("Estamos cargando los datos de su vehiculo.", size="8"), loading=True),
        rx.container(
            rx.skeleton(
                data_list("", "", "", "", "", "", "", "", ""),
                height="550px", width="100%", loading=True
            ),
            size="4",
            width="100%",
            height="100%"
        ),
        align="center",
        margin="12px",
        width="100%",
        spacing=Spacing.BIG.value,
        padding=Size.DEFAULT.value,
    )
