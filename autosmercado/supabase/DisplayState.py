import reflex as rx
from typing import Optional

from autosmercado.supabase.vehiculo import Vehiculo
from autosmercado.supabase.api import coche_info


class DisplayState(rx.State):
    car_loading: bool = True
    vehiculo_info: Optional[Vehiculo] = None

    @rx.event
    async def get_car(self):
        self.car_loading = True

        args = self.router.page.params
        categoria = args.get("category", [])

        self.vehiculo_info = await coche_info(categoria[0].replace("-", " "))

        if self.vehiculo_info is not None:
            self.car_loading = False
