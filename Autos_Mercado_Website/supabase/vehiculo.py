import reflex as rx
from typing import Optional


class Vehiculo(rx.Base):
    modelo: str
    url_modelo: str
    imagen_public_url: str
    precio_venta: Optional[int]
    precio_financiado: Optional[int]
