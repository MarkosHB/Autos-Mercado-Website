import reflex as rx


def accordion(header1: str, header2: str, header3: str,
              texto1: str, texto2: str, texto3: str) -> rx.Component:
    return rx.accordion.root(
        rx.accordion.item(
            header=rx.heading(header1, color_scheme="blue"),
            content=rx.text(
                texto1,
                text_align="justify",
                color=rx.color_mode_cond(light="black", dark="white"),
                padding="12px",
                ),
            value="casilla_1",
        ),
        rx.accordion.item(
            header=rx.heading(header2, color_scheme="blue"),
            content=rx.text(
                texto2,
                text_align="justify",
                color=rx.color_mode_cond(light="black", dark="white"),
                padding="12px",
            ),
            value="casilla_2",
        ),
        rx.accordion.item(
            header=rx.heading(header3, color_scheme="blue"),
            content=rx.text(
                texto3,
                text_align="justify",
                color=rx.color_mode_cond(light="black", dark="white"),
                padding="12px",
            ),
            value="casilla_3",
        ),
        type="single",
        collapsible=True,
        show_dividers=True,
        color_scheme="gray",
        variant="surface",
        radius="full",
        width="100%",
    )
