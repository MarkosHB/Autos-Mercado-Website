import reflex as rx
from typing import Optional


class Vehiculo(rx.Base):
    # Datos generales.
    modelo: str
    url_modelo: str
    imagen_public_url: str
    fotos: Optional[list]

    # Datos para la venta.
    precio_venta: str
    precio_financiado: str

    # Detalles del vehiculo.
    coches_punto_net: Optional[str]
    milanuncios: Optional[str]
    anio: Optional[str]
    tipo: Optional[str]
    combustible: Optional[str]
    transmision: Optional[str]
    kilometraje: Optional[str]
    caballos: Optional[str]
    cilindrada: Optional[str]
    puertas: Optional[str]
    color: Optional[str]
