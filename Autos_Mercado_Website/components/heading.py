import reflex as rx

from Autos_Mercado_Website.components.rectangle_content import rectangle_content
from Autos_Mercado_Website.styles.styles import Size


def heading(pagina: str, titulo: str, texto1="", texto2="") -> rx.Component:
    return rx.vstack(

        rx.blockquote(titulo, weight="bold", size="8", color_scheme="blue"),

        rx.tablet_and_desktop(

            rx.vstack(
                rectangle_content(texto1),
                #listado_compramos_tu_coche(),
                gap=Size.DEFAULT.value,
            ) if pagina == "COCHES_A_LA_CARTA" else rx.fragment(),

            rx.vstack(
                rectangle_content(texto1),
                #listado_compramos_tu_coche(),
                gap=Size.DEFAULT.value,
            ) if pagina == "COMPRAMOS_TU_COCHE" else rx.fragment(),

            rx.hstack(
                rectangle_content(texto1),
                rectangle_content(texto2),
                gap=Size.BIG.value,
            ) if pagina == "SOBRE_NOSOTROS" else rx.fragment(),

        ),

        rx.mobile_only(

            rx.vstack(
                rectangle_content(texto1),
                #listado_compramos_tu_coche(),
                gap=Size.DEFAULT.value,
            ) if pagina == "COCHES_A_LA_CARTA" else rx.fragment(),

            rx.vstack(
                rectangle_content(texto1),
                #listado_compramos_tu_coche(),
                gap=Size.DEFAULT.value,
            ) if pagina == "COMPRAMOS_TU_COCHE" else rx.fragment(),

            rx.vstack(
                rectangle_content(texto1),
                rectangle_content(texto2),
                gap=Size.VERY_SMALL.value,
            ) if pagina == "SOBRE_NOSOTROS" else rx.fragment(),

        ),
        width="100%",
    )


def listado_coches_a_la_carta() -> rx.Component:
    return rx.list(
        rx.list.item(
            rx.icon("circle_check_big", color="green"),
            " Allowed",
        ),
        rx.list.item(
            rx.icon("octagon_x", color="red"),
            " Not",
        ),
        rx.list.item(
            rx.icon("settings", color="grey"), " Settings"
        ),
        list_style_type="none",
    )


# Evaluamos tu coche y te damos las mejores recomendaciones
# Nos encargamos de todos los tramites y gestiones
# Te asesoramos y orientamos durante todo el proceso
def listado_compramos_tu_coche() -> rx.Component:
    return rx.list(
        rx.list.item(
            rx.icon("circle_check_big", color="green"),
            " Allowed",
        ),
        rx.list.item(
            rx.icon("octagon_x", color="red"),
            " Not",
        ),
        rx.list.item(
            rx.icon("settings", color="grey"), " Settings"
        ),
        list_style_type="none",
    )
