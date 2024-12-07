import reflex as rx

from Autos_Mercado_Website.pages.detallesvehiculo import detallesvehiculo
from Autos_Mercado_Website.pages.index import index
from Autos_Mercado_Website.pages.cochesalacarta import cochesalacarta
from Autos_Mercado_Website.pages.vendemossuvehiculo import vendemossuvehiculo
from Autos_Mercado_Website.pages.sobrenosotros import sobrenosotros
from Autos_Mercado_Website.pages.contacto import contacto


app = rx.App()

# Paginas Dinamicas:
app.add_page(detallesvehiculo)

# Paginas Estaticas:
app.add_page(index)
app.add_page(cochesalacarta)
app.add_page(vendemossuvehiculo)
app.add_page(sobrenosotros)
app.add_page(contacto)

