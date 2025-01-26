import reflex as rx


def data_list(v1, v2, v3, v4, v5, v6, v7, v8, v9) -> rx.Component:
    return rx.card(
        rx.data_list.root(
            rx.data_list.item(
                rx.data_list.label("🗓️ Año", color_scheme="blue"),
                rx.data_list.value(v1),
            ),
            rx.data_list.item(
                rx.data_list.label("🚗 Tipo", color_scheme="blue"),
                rx.data_list.value(v2),
            ),
            rx.data_list.item(
                rx.data_list.label("⛽ Combustible", color_scheme="blue"),
                rx.data_list.value(v3),
            ),
            rx.data_list.item(
                rx.data_list.label("⚙️ Transmisión", color_scheme="blue"),
                rx.data_list.value(v4),
            ),
            rx.data_list.item(
                rx.data_list.label("🛣️ Kilometraje ", color_scheme="blue"),
                rx.data_list.value(v5),
            ),
            rx.data_list.item(
                rx.data_list.label("🐎 Caballos", color_scheme="blue"),
                rx.data_list.value(v6),
            ),
            rx.data_list.item(
                rx.data_list.label("🚀 Cilindrada", color_scheme="blue"),
                rx.data_list.value(v7),
            ),
            rx.data_list.item(
                rx.data_list.label("🚪Puertas", color_scheme="blue"),
                rx.data_list.value(v8),
            ),
            rx.data_list.item(
                rx.data_list.label("🎨 Color", color_scheme="blue"),
                rx.data_list.value(v9),
            ),
            size="3",
            orientacion="horizontal"
        ),
        variant="classic"
    )
