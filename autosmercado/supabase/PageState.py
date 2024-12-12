from io import BytesIO

import reflex as rx
from autosmercado.supabase.api import coches_info
from autosmercado.supabase.vehiculo import Vehiculo

from PIL import Image
import urllib.request
from PIL.ImageFile import ImageFile


def obtener_imagen(url: str) -> ImageFile:
    peticion = urllib.request.Request(url)
    respuesta = urllib.request.urlopen(peticion)
    img = Image.open(respuesta)
    img.thumbnail((100, 100))
    webp_file = BytesIO()
    img.save(webp_file, format="WEBP", quality=85)
    webp_file.seek(0)
    return Image.open(webp_file)


class PageState(rx.State):
    loading: bool = True
    vehiculos_info: list[Vehiculo]
    preview_images: list[ImageFile]

    @rx.event
    async def get_data(self):
        if not self.vehiculos_info:
            self.loading = True

            self.vehiculos_info = await coches_info()

            self.loading = False
