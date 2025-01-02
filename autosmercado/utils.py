import reflex as rx
import qrcode
from PIL import Image, ImageDraw, ImageFont


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


title_index = "Inicio | Autos-Mercado"

title_cochesalacarta = "Coches a la carta | Autos-Mercado"

title_vendemossuvehiculo = "Vendemos su vehículo | Autos-Mercado"

title_sobrenosotros = "Sobre nosotros | Autos-Mercado"

title_contacto = "Contacto | Autos-Mercado"

title_detallesvehiculo = "Detalles del vehículo | Autos-Mercado"

MAX_FORM_MSGs = 10  # limite de mensajes recibidos en el formulario


def generar_codigo(url: str, fichero: str) -> Image:
    """ Funcion que define el proceso de creación del QR.

    Args:
        url (str): La direccion en sí misma.
        fichero (str): El nombre del archivo.
    """

    # Marco inicial de la imagen.
    codigo = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Generador del codigo.
    codigo.add_data(url)
    codigo.make(fit=True)
    img = codigo.make_image(fill="black", back_color="white").convert("RGB")

    # Introducimos el titulo inferior.
    return dibujar_titulo(img, fichero)  # (Opcional).


def dibujar_titulo(img: Image, titulo: str) -> Image:
    """Funcion auxiliar para dibujar el titulo identificativo inferior del codigo.

    Args:
        img (Image): La imagen original sin redimensionar.
        titulo (str): El rotulo a plasmar.
    """

    # Reajustes en la imagen.
    ancho, alto = img.size
    alto_total = alto + 50
    nueva_imagen = Image.new("RGB", (ancho, alto_total), "white")
    nueva_imagen.paste(img, (0, 0, ancho, alto))

    # Seleccion de la tipografia.
    draw = ImageDraw.Draw(nueva_imagen)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    # Añadir el titulo debajo del QR.
    text_width = draw.textlength(titulo, font=font)
    text_x = (ancho - text_width) // 2
    text_y = alto + 10
    draw.text((text_x, text_y), titulo, fill="black", font=font)

    return nueva_imagen
