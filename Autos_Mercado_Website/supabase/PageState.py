import reflex as rx
from Autos_Mercado_Website.supabase.api import coches_info, coche_info
from Autos_Mercado_Website.supabase.vehiculo import Vehiculo

from PIL import Image
import urllib.request
from PIL.ImageFile import ImageFile


def obtener_imagen(url: str):
    if url == "https://lspvlivxftanwjnkkgcz.supabase.co/storage/v1/object/public/imagenesCoches/":
        return "logo.png"
    else:
        peticion = urllib.request.Request(url)
        respuesta = urllib.request.urlopen(peticion)
        return Image.open(respuesta)


class PageState(rx.State):
    loading: bool = True
    vehiculos_info: list[Vehiculo]
    preview_images: list  # [ImageFile]

    car_loading: bool = True
    vehiculo_info: Vehiculo = None
    modelo: str = None
    image: ImageFile = None

    @rx.event
    async def get_data(self):
        self.loading = True

        self.vehiculos_info = await coches_info()
        for coche in self.vehiculos_info:
            self.preview_images.append(obtener_imagen(coche.imagen_public_url))

        self.loading = False

    @rx.event
    async def get_car(self):
        self.car_loading = True

        args = self.router.page.params
        modelo = args.get("category", [])

        self.vehiculo_info = await coche_info(modelo[0].replace("-", " "))
        self.image = obtener_imagen(self.vehiculo_info.imagen_public_url)

        self.car_loading = False

