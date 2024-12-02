import reflex as rx

from Autos_Mercado_Website.components.form import form
from Autos_Mercado_Website.routes import Route
from Autos_Mercado_Website.styles.colors import TextColor
from Autos_Mercado_Website.styles.styles import Size, Spacing, Color
from Autos_Mercado_Website.components.title import title

FONT_SIZE = [Size.DEFAULT_MEDIUM.value, Size.DEFAULT_BIG.value]


def navbar(route: Route) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="/logo.png",
                alt="Logotipo de Autos-mercado."
            ),
            rx.spacer(),
            rx.desktop_only(
                rx.hstack(
                    rx.spacer(),
                    _menu_inicio(route),
                    _menu_cochesalacarta(route),
                    _menu_vendemossuvehiculo(route),
                    _menu_sobrenosotros(route),
                    _dialog_formulario(),
                    spacing=Spacing.BIG.value
                ),
                width="100%",
                padding=Size.BIG.value,
            ),
            rx.mobile_and_tablet(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.flex(
                            rx.icon("align-justify", size=40, color="white")
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item(
                            _menu_inicio(route),
                            background="transparent"
                        ),
                        rx.menu.item(
                            _menu_cochesalacarta(route),
                            backbround="transparent"
                        ),
                        rx.menu.item(
                            _menu_vendemossuvehiculo(route),
                            backbround="transparent"
                        ),
                        rx.menu.item(
                            _menu_sobrenosotros(route),
                            backbround="transparent"
                        ),
                        rx.menu.item(
                            _pagina_formulario(route),
                            backbround="transparent"
                        ),
                        background=Color.SECONDARY.value,
                        border_color=Color.PRIMARY.value,
                        minWidth="100px"
                    ),
                )
            ),
            width="100%",
            align="center"
        ),
        bg=Color.SECONDARY.value,
        position="sticky",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )


def _menu_inicio(route: Route) -> rx.Component:
    return rx.link(
        title(
            "Inicio",
            size=[Size.DEFAULT_BIG.value],
            color=TextColor.RED if route == Route.INDEX else TextColor.PRIMARY
        ),
        href=Route.INDEX.value
    )


def _menu_cochesalacarta(route: Route) -> rx.Component:
    return rx.link(
        title(
            "Coches a la carta",
            size=[Size.DEFAULT_BIG.value],
            color=TextColor.RED if route == Route.COCHESALACARTA else TextColor.PRIMARY
        ),
        href=Route.COCHESALACARTA.value
    )


def _menu_vendemossuvehiculo(route: Route) -> rx.Component:
    return rx.link(
        title(
            "Vendemos su vehículo",
            size=[Size.DEFAULT_BIG.value],
            color=TextColor.RED if route == Route.VENDEMOSSUVEHICULO else TextColor.PRIMARY
        ),
        href=Route.VENDEMOSSUVEHICULO.value
    )


def _menu_sobrenosotros(route: Route) -> rx.Component:
    return rx.link(
        title(
            "Sobre nosotros",
            size=[Size.DEFAULT_BIG.value],
            color=TextColor.RED if route == Route.SOBRENOSOTROS else TextColor.PRIMARY
        ),
        href=Route.SOBRENOSOTROS.value
    )


def _pagina_formulario(route: Route) -> rx.Component:
    # Funcion para crear una pagina solo en modo movil.
    return rx.link(
        title(
            "Contacto",
            size=[Size.DEFAULT_BIG.value],
            color=TextColor.RED if route == Route.CONTACTO else TextColor.PRIMARY
        ),
        href=Route.CONTACTO.value
    )


def _dialog_formulario() -> rx.Component:
    # Funcion para crear un dialog en desktop y tablet.
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                title(
                    "Contacto",
                    size=[Size.DEFAULT_BIG.value],
                ),
                color_scheme="blue",
                variant="classic",
                radius="large",
                size="3",
            ),
        ),
        rx.dialog.content(
            form(),
        ),
        margin="20px"
    )


