import reflex as rx
from Autos_Mercado_Website.components.title import title
from Autos_Mercado_Website.styles.styles import Size, Spacing


def cochesnet_milanuncios(link1: str, link2: str) -> rx.Component:
    return rx.flex(
        rx.button(
            rx.link(
                title("Coches.net", size=[Size.DEFAULT_BIG.value]),
                href=link1
            ),
            radius="large",
            size="2",
            color_scheme="red",
            variant="solid"
        ),
        rx.button(
            rx.link(
                title("Milanuncios", size=[Size.DEFAULT_BIG.value]),
                href=link2
            ),
            radius="large",
            size="2",
            color_scheme="jade",
            variant="solid"
        ),
        spacing=Spacing.BIG.value,
        padding=Size.BIG.value,
        width="100%",
        flex_wrap="wrap",
        justify="center"
    )
