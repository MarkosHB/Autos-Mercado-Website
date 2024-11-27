import reflex as rx


def header() -> rx.Component:
    return rx.box(
        rx.heading("Welcome to Autos-Mercado!", size="9"),
    )
