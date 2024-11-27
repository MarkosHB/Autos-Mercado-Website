import reflex as rx
import Autos_Mercado_Website.constants as const
from Autos_Mercado_Website.components.tarjeta import tarjeta
from Autos_Mercado_Website.styles.styles import Size, Spacing, Color, TextColor, Font


def footer() -> rx.Component:
    return rx.flex(
        tarjeta("Phone", TextColor.GREEN, None, const.MOVIL1),
        tarjeta("Phone", TextColor.GREEN, None, const.MOVIL2),
        tarjeta("Mail", TextColor.PURPLE, None, const.CORREO_ELECTRONICO),
        tarjeta("Instagram", TextColor.PINK, const.INSTAGRAM, "@autos_mercado"),
        tarjeta("Facebook", TextColor.BLUE, const.FACEBOOK, "@autosmercadovelez"),
        tarjeta("car", TextColor.SECONDARY, const.COCHES_PUNTO_NET, "Coches.net"),
        tarjeta("car-front", TextColor.SECONDARY, const.MILANUNCIOS, "Milanuncios"),

        bg=Color.SECONDARY.value,
        spacing=Spacing.BIG.value,
        border_top=f"1px solid {Color.SECONDARY.value}",
        padding=Size.BIG.value,
        width="100%",
        flex_wrap="wrap",
        justify="center"
    )
