from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)
import reflex as rx


status_chip_props = {
    "radius": "full",
    "variant": "outline",
    "size": "3",
}


def status_chip(
    status: str, icon: str, color: LiteralAccentColor
) -> rx.Component:
    return rx.badge(
        rx.icon(icon, size=18),
        status,
        color_scheme=color,
        **status_chip_props,
    )
