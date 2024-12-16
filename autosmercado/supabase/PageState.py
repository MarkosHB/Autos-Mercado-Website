import reflex as rx
from autosmercado.supabase.api import coches_info
from autosmercado.supabase.vehiculo import Vehiculo


class PageState(rx.State):
    loading: bool = True
    vehiculos_info: list[Vehiculo]

    @rx.event
    async def get_data(self):
        if not self.vehiculos_info:
            self.loading = True

            self.vehiculos_info = await coches_info()

            self.loading = False
