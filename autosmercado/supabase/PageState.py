import reflex as rx
from autosmercado.supabase.api import coches_info
from autosmercado.supabase.vehiculo import Vehiculo
from autosmercado.supabase.api import enviar_mensaje_formulario
from datetime import datetime


class PageState(rx.State):
    loading: bool = True
    vehiculos_info: list[Vehiculo]

    form_data: dict = {}

    @rx.event
    async def handle_submit(self, form_data: dict):
        form_data["fecha_envio"] = datetime.now().strftime("%d/%m/%Y")

        self.form_data = form_data

        await enviar_mensaje_formulario(form_data)

    @rx.event
    async def get_data(self):
        self.loading = True
        self.vehiculos_info = await coches_info()
        self.loading = False
