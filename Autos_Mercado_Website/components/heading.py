import reflex as rx

from Autos_Mercado_Website.components.rectangle_content import rectangle_content
from Autos_Mercado_Website.styles.styles import Size, Spacing
import Autos_Mercado_Website.texts as texto


def heading(pagina: str, titulo: str, texto1="", texto2="") -> rx.Component:
    return rx.vstack(

        rx.blockquote(titulo, weight="bold", size="8", color_scheme="blue"),

        rx.tablet_and_desktop(

            rx.vstack(
                rectangle_content(texto1),
                callout_coches_a_la_carta(),
                rectangle_content(texto2),
                gap=Size.DEFAULT.value,
            ) if pagina == "COCHES_A_LA_CARTA" else rx.fragment(),

            rx.vstack(
                rectangle_content(texto1),
                listado_vendemos_su_vehiculo(),
                callout_vendemos_su_vehiculo(),
                gap=Size.DEFAULT.value,
            ) if pagina == "VENDEMOS_SU_VEHICULO" else rx.fragment(),

            rx.hstack(
                rectangle_content(texto1),
                rectangle_content(texto2),
                gap=Size.BIG.value,
            ) if pagina == "SOBRE_NOSOTROS" else rx.fragment(),

        ),

        rx.mobile_only(

            rx.vstack(
                rectangle_content(texto1),
                callout_coches_a_la_carta(),
                rectangle_content(texto2),
                gap=Size.DEFAULT.value,
            ) if pagina == "COCHES_A_LA_CARTA" else rx.fragment(),

            rx.vstack(
                rectangle_content(texto1),
                listado_vendemos_su_vehiculo(),
                callout_vendemos_su_vehiculo(),
                gap=Size.DEFAULT.value,
            ) if pagina == "VENDEMOS_SU_VEHICULO" else rx.fragment(),

            rx.vstack(
                rectangle_content(texto1),
                rectangle_content(texto2),
                gap=Size.ZERO.value,
            ) if pagina == "SOBRE_NOSOTROS" else rx.fragment(),

        ),
        width="100%",
    )


def callout_coches_a_la_carta() -> rx.Component:
    return rx.callout(
        rx.text(
            texto.COCHES_A_LA_CARTA_CALLOUT,
            size="3",
        ),
        icon="info",
        color_scheme="gray",
        padding=Size.MEDIUM.value,
    )


def callout_vendemos_su_vehiculo() -> rx.Component:
    return rx.flex(
        rx.callout(
            rx.text(
                texto.VENDEMOS_SU_VEHICULO_CALLOUT1,
                size="3",
            ),
            icon="check",
            color_scheme="green",
        ),
        rx.callout(
            rx.text(
                texto.VENDEMOS_SU_VEHICULO_CALLOUT2,
                size="3",
            ),
            icon="smile",
            color_scheme="yellow",
        ),
        flex_wrap="wrap",
        spacing=Spacing.DEFAULT.value,
        padding=Size.MEDIUM.value,
    )


def listado_vendemos_su_vehiculo() -> rx.Component:
    return rx.list.unordered(
        rx.list.item(
            rx.text(
                texto.VENDEMOS_SU_VEHICULO_LISTADO1,
                size="4",
            ),
        ),
        rx.list.item(
            rx.text(
                texto.VENDEMOS_SU_VEHICULO_LISTADO2,
                size="4",
            ),
        ),
        list_style_type="disc",
        padding=Size.MEDIUM.value,
    )
