import reflex as rx

from Autos_Mercado_Website.supabase.vehiculo import Vehiculo
from Autos_Mercado_Website.supabase.api import coche_info
from PIL import Image
import urllib.request
from PIL.ImageFile import ImageFile


def obtener_imagen(url: str):
    peticion = urllib.request.Request(url)
    respuesta = urllib.request.urlopen(peticion)
    return Image.open(respuesta)


class DisplayState(rx.State):
    car_loading: bool = True
    vehiculo_info: Vehiculo = None
    modelo: str = None
    image: ImageFile = None

    @rx.event
    async def get_car(self):
        self.car_loading = True

        args = self.router.page.params
        modelo = args.get("category", [])

        self.vehiculo_info = await coche_info(modelo[0].replace("-", " "))
        self.image = obtener_imagen(self.vehiculo_info.imagen_public_url)

        self.car_loading = False
