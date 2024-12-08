from enum import Enum


class Route(Enum):
    INDEX = "/"
    COCHESALACARTA = "/coches-a-la-carta"
    VENDEMOSSUVEHICULO = "/vendemos-su-vehiculo"
    SOBRENOSOTROS = "/sobre-nosotros"
    CONTACTO = "/contacto"
    DETALLESVEHICULO = "/detalles-del-vehiculo/[...category]"
