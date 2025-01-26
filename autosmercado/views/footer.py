import reflex as rx
import autosmercado.constants as const
from autosmercado.components.social_link import social_link
from autosmercado.styles.styles import Size, Spacing, Color, TextColor


def footer() -> rx.Component:
    return rx.flex(
        social_link("Smartphone", TextColor.GREEN, f"tel:+{const.MOVIL1}", const.MOVIL1),
        social_link("Smartphone", TextColor.GREEN, f"tel:+{const.MOVIL2}", const.MOVIL2),
        social_link("Phone", TextColor.GREEN, f"tel:+{const.FIJO}", const.FIJO),
        social_link("Mail", TextColor.PURPLE, f"mailto:{const.CORREO_ELECTRONICO}", const.CORREO_ELECTRONICO),
        social_link("Instagram", TextColor.PINK, const.INSTAGRAM, "@autos_mercado"),
        social_link("Facebook", TextColor.BLUE, const.FACEBOOK, "Autos-Mercado.com"),
        bg=Color.SECONDARY.value,
        spacing=Spacing.BIG.value,
        margin_top="30px",
        border_top=f"1px solid {Color.SECONDARY.value}",
        padding=Size.BIG.value,
        width="100%",
        flex_wrap="wrap",
        justify="center"
    )
