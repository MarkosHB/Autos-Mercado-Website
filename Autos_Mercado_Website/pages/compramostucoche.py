import reflex as rx

import Autos_Mercado_Website.utils as utils
from Autos_Mercado_Website.routes import Route

from Autos_Mercado_Website.styles.styles import Size, Spacing
from Autos_Mercado_Website.styles.colors import TextColor


from Autos_Mercado_Website.views.navbar import navbar
from Autos_Mercado_Website.views.header import header
from Autos_Mercado_Website.views.formulario_contacto import formulario_contacto
from Autos_Mercado_Website.views.footer import footer


ROUTE = Route.COMPRAMOSTUCOCHE


@rx.page(
    title=utils.title_compramostucoche,
    route=ROUTE.value,
)
def compramostucoche() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    titulo="Compramos tu Coche",
                    text1="Utiliza el lenguaje de programación que tú quieras para resolver ejercicios que te ayudarán a mejorar tu forma de pensar y enfrentarte a retos de código.",
                    text2="Consulta correcciones de la comunidad en los repositorios de código de los diferentes retos. Se han dividido entre los resueltos en 2022 y 2023 (consulta su etiqueta).",
                ),
                formulario_contacto(),
                footer(),
                spacing=Spacing.VERY_BIG.value,
                align="center",
                width="100%"
            )
        )
    )
