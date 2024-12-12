import reflex as rx
from autosmercado.supabase.api import coches_info
from autosmercado.supabase.vehiculo import Vehiculo

from PIL import Image
import urllib.request
from PIL.ImageFile import ImageFile


def obtener_imagen(url: str):
    peticion = urllib.request.Request(url)
    respuesta = urllib.request.urlopen(peticion)
    return Image.open(respuesta)


class PageState(rx.State):
    loading: bool = True
    vehiculos_info: list[Vehiculo]
    preview_images: list[ImageFile]

    @rx.event
    async def get_data(self):
        if not self.vehiculos_info:
            self.loading = True

            self.vehiculos_info = await coches_info()
            for coche in self.vehiculos_info:
                self.preview_images.append(obtener_imagen(coche.imagen_public_url))

            self.loading = False
