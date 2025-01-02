import reflex as rx
from typing import Optional

from autosmercado.supabase.vehiculo import Vehiculo
from autosmercado.supabase.api import coche_info
from autosmercado.utils import generar_codigo
from io import BytesIO


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

    @rx.event
    def descargar_qr(self):
        args = self.router.page.params
        categoria = args.get("category", [])
        fichero = categoria[0].replace("-", " ")

        qr = generar_codigo(url=self.router.page.full_raw_path, fichero=fichero)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)  # Volver al inicio del buffer para leer los datos.

        return rx.download(
            data=buffer.read(),
            filename=f"{fichero}.png",
        )
