import reflex as rx
import Autos_Mercado_Website.constants as const
from Autos_Mercado_Website.components.social_link import social_link
from Autos_Mercado_Website.styles.styles import Size, Spacing, Color, TextColor, Font


def footer() -> rx.Component:
    return rx.flex(
        social_link("Smartphone", TextColor.GREEN, None, const.MOVIL1),
        social_link("Smartphone", TextColor.GREEN, None, const.MOVIL2),
        social_link("Phone", TextColor.GREEN, None, const.FIJO),
        social_link("Mail", TextColor.PURPLE, None, const.CORREO_ELECTRONICO),
        social_link("Instagram", TextColor.PINK, const.INSTAGRAM, "@autos_mercado"),
        social_link("Facebook", TextColor.BLUE, const.FACEBOOK, "@autosmercadovelez"),
        social_link("car", TextColor.SECONDARY, const.COCHES_PUNTO_NET, "Coches.net"),
        social_link("car-front", TextColor.SECONDARY, const.MILANUNCIOS, "Milanuncios"),

        bg=Color.SECONDARY.value,
        spacing=Spacing.BIG.value,
        margin_top="20px",
        border_top=f"1px solid {Color.SECONDARY.value}",
        padding=Size.BIG.value,
        width="100%",
        flex_wrap="wrap",
        justify="center"
    )
