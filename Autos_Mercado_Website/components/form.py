import reflex as rx


class FormInputState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        self.form_data = form_data


def form_field(
    label: str, placeholder: str, type: str, name: str
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


def form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Contacte con nuestro equipo",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Indíquenos el motivo por el que nos escribe.",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.select(
                        [
                            "Interesad@ en un vehículo de Stock",
                            "Servicio: Coches a la carta",
                            "Servicio: Vendemos su vehículo",
                            "Consulta adicional no contemplada"
                         ],
                        default_value="Interesad@ en un vehículo de Stock",
                        name="motivo de consulta",
                        required=True,
                    ),
                    rx.flex(
                        form_field(
                            "Nombre.",
                            "Su nombre de pila",
                            "text",
                            "Nombre del interesado",
                        ),
                        form_field(
                            "Apellidos.",
                            "Su apellido completo",
                            "text",
                            "Apellidos",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "Correo electrónico.",
                            "Su email de uso habitual",
                            "text",
                            "email",
                        ),
                        form_field(
                            "Teléfono.", "Su número de teléfono", "text", "telefono"
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.text(
                            "Mensaje.",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Motivo de contacto, datos relevantes...",
                            name="mensaje",
                            resize="vertical",
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.dialog.close(  # Por estar en un dialog.
                            rx.button("Enviar información"),
                            on_click=rx.toast.success(
                                "¡Formulario enviado correctamente!",
                                position="bottom-right",
                            ),
                            width="100%",
                        ),
                        variant="soft",
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=lambda form_data: rx.window_alert(
                    form_data.to_string()
                ),
                reset_on_submit=True,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
        variant="ghost",
    )


def mobile_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Contacte con nuestro equipo",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Indíquenos el motivo por el que nos escribe.",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.select(
                        [
                            "Interesad@ en un vehículo de Stock",
                            "Servicio: Coches a la carta",
                            "Servicio: Vendemos su vehículo",
                            "Consulta adicional no contemplada"
                         ],
                        default_value="Interesad@ en un vehículo de Stock",
                        name="motivo de consulta",
                        required=True,
                    ),
                    rx.flex(
                        form_field(
                            "Nombre.",
                            "Su nombre de pila",
                            "text",
                            "Nombre del interesado",
                        ),
                        form_field(
                            "Apellidos.",
                            "Su apellido completo",
                            "text",
                            "Apellidos",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "Correo electrónico.",
                            "Su email de uso habitual",
                            "text",
                            "email",
                        ),
                        form_field(
                            "Teléfono.", "Su número de teléfono", "text", "telefono"
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.text(
                            "Mensaje.",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Motivo de contacto, datos relevantes...",
                            name="mensaje",
                            resize="vertical",
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button(
                            "Enviar información",
                            width="100%",
                        ),
                        on_click=rx.toast.success(
                            "¡Formulario enviado correctamente!",
                            position="bottom-right",
                        ),
                        variant="soft",
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=lambda form_data: rx.window_alert(
                    form_data.to_string()
                ),
                reset_on_submit=True,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
        variant="surface",
    )
