import reflex as rx
from typing import Optional

from autosmercado.supabase.vehiculo import Vehiculo
from autosmercado.supabase.api import coche_info
from PIL import Image
import urllib.request
from PIL.ImageFile import ImageFile


def obtener_imagen(url: str):
    peticion = urllib.request.Request(url)
    respuesta = urllib.request.urlopen(peticion)
    return Image.open(respuesta)


class DisplayState(rx.State):
    car_loading: bool = True
    vehiculo_info: Optional[Vehiculo] = None
    modelo: str = ""

    @rx.event
    async def get_car(self):
        self.car_loading = True

        args = self.router.page.params
        categoria = args.get("category", [])

        if self.modelo != categoria[0]:
            self.modelo = categoria[0]

            self.vehiculo_info = await coche_info(self.modelo.replace("-", " "))

        self.car_loading = False
