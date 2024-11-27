import reflex as rx
import Autos_Mercado_Website.styles.styles as styles
from Autos_Mercado_Website.styles.styles import Size
from Autos_Mercado_Website.styles.colors import TextColor
from Autos_Mercado_Website.styles.fonts import Font, FontWeight


def title(
    text: str,
    font=Font.DEFAULT,
    weight=FontWeight.BOLD,
    size=[Size.DEFAULT_BIG.value],
    color=TextColor.PRIMARY,
    negative_margin=False
) -> rx.Component:
    return rx.text(
        text,
        font_family=font.value,
        font_weight=weight.value,
        font_size=size,
        color=color.value,
        custom_attrs={
            styles.CustomAttrs.DATA_TEXT.value: text,
        },
        #style=styles.glow_text_style,
        margin_top=f"-{Size.VERY_SMALL.value}" if negative_margin else None
    )
