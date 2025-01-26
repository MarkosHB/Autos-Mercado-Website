import reflex as rx

from autosmercado.components.social_link import social_link
from autosmercado.styles.styles import Color, Spacing, Size, TextColor
import autosmercado.constants as const


def welcome() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/fachada.jpg",
            border_radius="20px 20px",
            border="2px solid white",
        ),
        rx.tablet_and_desktop(
            rx.flex(
                social_link("Smartphone", TextColor.GREEN, f"tel:+{const.MOVIL1}", const.MOVIL1),
                social_link("Smartphone", TextColor.GREEN, f"tel:+{const.MOVIL2}", const.MOVIL2),
                social_link("Phone", TextColor.GREEN, f"tel:+{const.FIJO}", const.FIJO),
                social_link("Mail", TextColor.PURPLE, f"mailto:{const.CORREO_ELECTRONICO}", const.CORREO_ELECTRONICO),

                spacing=Spacing.BIG.value,
                border_top=f"1px solid {Color.SECONDARY.value}",
                padding=Size.BIG.value,
                width="100%",
                flex_wrap="wrap",
                justify="center"
            ),
        ),
        width="100%",
        padding="32px",
        align="center",
        background=Color.SECONDARY.value
    )
