import reflex as rx

from Autos_Mercado_Website.styles.colors import TextColor
from Autos_Mercado_Website.styles.styles import Size, Spacing
from Autos_Mercado_Website.styles.fonts import FontWeight


def heading(title: str, body1="", body2="") -> rx.Component:
    return rx.vstack(
        rx.blockquote(title, weight="bold", size="8", color_scheme="blue"),
        rx.grid(
            _paragraph_text(body1),
            _paragraph_text(body2),
            rows="1",
            columns="2",
            width="100%",
            gap=Size.MEDIUM_BIG.value
        ),
        rx.separator(),
        spacing=Spacing.BIG.value,
        padding_x=Size.ZERO.value,
        width="100%"
    )


def _paragraph_text(text: str) -> rx.Component:
    return rx.box(
        rx.text(
            text,
            font_size=Size.DEFAULT_MEDIUM.value,
            font_weight=FontWeight.MEDIUM.value
        ),
        row_span=1,
        col_span=1
    )
