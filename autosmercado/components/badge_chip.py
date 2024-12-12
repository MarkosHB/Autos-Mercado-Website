from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)
import reflex as rx


def badge_chip(msg: str, color: LiteralAccentColor) -> rx.Component:
    return rx.badge(
        msg,
        color_scheme=color,
        radius="full",
        variant="soft",
        size="3",
    )
