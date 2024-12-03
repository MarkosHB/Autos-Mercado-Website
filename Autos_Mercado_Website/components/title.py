import reflex as rx
from Autos_Mercado_Website.styles.styles import Size, TextColor, FontWeight


def title(
    text: str,
    font="Mona Sans",
    weight=FontWeight.BOLD.value,
    size=[Size.DEFAULT_BIG.value],
    color=TextColor.PRIMARY,
    negative_margin=False
) -> rx.Component:
    return rx.text(
        text,
        font_family=font,
        font_weight=weight,
        font_size=size,
        color=color.value,
        custom_attrs={
            "datatext": text,
        },
        margin_top=f"-{Size.VERY_SMALL.value}" if negative_margin else None
    )
