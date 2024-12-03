import reflex as rx

from Autos_Mercado_Website.styles.styles import Spacing


# TODO rx.skeleton()
def car_preview(idx: int, modelo: str, ) -> rx.Component:
    return rx.link(
        rx.card(
            rx.inset(
                rx.image(
                    src="/logo.png",
                    width="100%",
                    height="auto",
                ),
                side="top",
                pb="current",
                clip="padding-box",
            ),
            rx.heading(
                modelo
            ),
            rx.text(
                "Prueba",
            ),
            width="100%",
            spacing=Spacing.DEFAULT.value,
        ),
        href="",
    )
