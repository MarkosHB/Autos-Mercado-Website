import reflex as rx
from Autos_Mercado_Website.supabase.api import coches
from Autos_Mercado_Website.supabase.vehiculo import Vehiculo


class PageState(rx.State):
    vehiculo_info: list[Vehiculo]

    async def get_data(self):
        self.vehiculo_info = await coches()
