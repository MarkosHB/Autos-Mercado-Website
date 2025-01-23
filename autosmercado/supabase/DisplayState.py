import reflex as rx
from typing import Optional

from autosmercado.supabase.vehiculo import Vehiculo
from autosmercado.supabase.api import coche_info
from autosmercado.utils import generar_codigo
from io import BytesIO


class DisplayState(rx.State):
    car_loading: bool = True
    vehiculo_info: Optional[Vehiculo] = None
    current_image_idx: int = 0
    hay_fotos: bool = False

    @rx.event
    async def get_car(self):
        self.car_loading = True

        args = self.router.page.params
        categoria = args.get("category", [])

        self.vehiculo_info = await coche_info(categoria[0].replace("-", " "))

        if self.vehiculo_info is not None:
            self.hay_fotos = len(self.vehiculo_info.fotos) > 0
            self.car_loading = False
        else:
            yield rx.toast.error(
                "Error: No se ha encontrado ningún vehículo en esta dirección. Compruebe si es correcta.",
                duration=5000,
                close_button=True,
                position="bottom-right",
            )
        
    @rx.event
    def previous_image(self): 
        self.current_image_idx = (self.current_image_idx - 1) % len(self.vehiculo_info.fotos)
    
    @rx.event
    def next_image(self): 
        self.current_image_idx = (self.current_image_idx + 1) % len(self.vehiculo_info.fotos)

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
