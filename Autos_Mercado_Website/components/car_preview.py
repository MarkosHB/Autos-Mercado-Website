import reflex as rx


# TODO rx.skeleton()
def car_preview() -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src="/fachada.jpg",
                width="100%",
                height="auto",
            ),
            side="top",
            pb="current",
        ),
        rx.text(
            "Reflex is a web framework that allows developers to build their app in pure Python."
        ),
        width="25vw",
    )
