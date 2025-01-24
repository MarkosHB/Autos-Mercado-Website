import reflex as rx

from autosmercado.pages.detallesvehiculo import detallesvehiculo
from autosmercado.pages.index import index
from autosmercado.pages.cochesalacarta import cochesalacarta
from autosmercado.pages.pantallapresentacion import pantallapresentacion
from autosmercado.pages.vendemossuvehiculo import vendemossuvehiculo
from autosmercado.pages.sobrenosotros import sobrenosotros
from autosmercado.pages.contacto import contacto


app = rx.App()

# Paginas Dinamicas:
app.add_page(detallesvehiculo)
app.add_page(pantallapresentacion)

# Paginas Estaticas:
app.add_page(index)
app.add_page(cochesalacarta)
app.add_page(vendemossuvehiculo)
app.add_page(sobrenosotros)
app.add_page(contacto)

