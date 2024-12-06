import reflex as rx
from Autos_Mercado_Website.supabase.api import coche_info
from Autos_Mercado_Website.supabase.vehiculo import Vehiculo

from PIL import Image
import urllib.request
from PIL.ImageFile import ImageFile


def obtener_imagen(url: str) -> ImageFile:
    peticion = urllib.request.Request(url)
    respuesta = urllib.request.urlopen(peticion)
    return Image.open(respuesta)


class PageState(rx.State):
    loading: bool = True
    vehiculo_info: list[Vehiculo]
    preview_images: list[ImageFile]

    async def get_data(self):
        self.loading = True
        self.vehiculo_info = await coche_info()

        for coche in self.vehiculo_info:
            self.preview_images.append(obtener_imagen(coche.imagen_public_url))

        self.loading = False
