import reflex as rx


def rectangle_content() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.heading("Saving Money"),
            rx.text(
                "Saving money is an art that combines discipline, strategic planning, and the wisdom to foresee future needs and emergencies. It begins with the simple act of setting aside a portion of one's income, creating a buffer that can grow over time through interest or investments.",
                margin_top="0.5em",
            ),
            padding="1em",
            border_width="1px",
        ),
        rx.box(
            rx.heading("Spending Money"),
            rx.text(
                "Spending money is a balancing act between fulfilling immediate desires and maintaining long-term financial health. It's about making choices, sometimes indulging in the pleasures of the moment, and at other times, prioritizing essential expenses.",
                margin_top="0.5em",
            ),
            padding="1em",
            border_width="1px",
        ),
        rx.box(
            rx.heading("Spending Money"),
            rx.text(
                "Spending money is a balancing act between fulfilling immediate desires and maintaining long-term financial health. It's about making choices, sometimes indulging in the pleasures of the moment, and at other times, prioritizing essential expenses.",
                margin_top="0.5em",
            ),
            padding="1em",
            border_width="1px",
        ),
        gap="2em",
    )
