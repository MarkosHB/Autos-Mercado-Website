import os
import dotenv
from supabase import create_client, Client
from autosmercado.supabase.vehiculo import Vehiculo


class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    SUPABASE_TABLE = os.environ.get("SUPABASE_TABLE")
    SUPABASE_BUCKET = os.environ.get("SUPABASE_BUCKET")

    SUPABASE_FORM = os.environ.get("SUPABASE_FORM")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    def fetch_data(self):
        response = (
            self.supabase.table(self.SUPABASE_TABLE)
            .select("nombre, imagen, precio_venta, precio_financiado")
            .filter('check_anunciado', 'eq', True)
            .filter('check_vendido', 'eq', False)
            .execute()
        )

        vehiculo_data = []

        if len(response.data) > 0:
            for coche in response.data:
                vehiculo_data.append(
                    Vehiculo(
                        modelo=coche["nombre"],
                        url_modelo=str(coche["nombre"]).replace(" ", "-"),
                        imagen_public_url=self.imagen_preview(coche["imagen"]),
                        precio_venta=f"{int(coche['precio_venta']):,.0f}".replace(",", "."),
                        precio_financiado=f"{int(coche['precio_financiado']):,.0f}".replace(",", "."),
                    )
                )

        return vehiculo_data

    def fetch_car(self, modelo: str):
        response = (
            self.supabase.table(self.SUPABASE_TABLE)
            .select("nombre, imagen, precio_venta, precio_financiado, coches_punto_net, milanuncios, anio, tipo, "
                    "combustible, transmision, kilometraje, caballos, cilindrada, puertas, color")
            .filter('nombre', 'eq', modelo)
            .filter('check_anunciado', 'eq', True)
            .filter('check_vendido', 'eq', False)
            .execute()
        )

        vehiculo = None

        if len(response.data) > 0:
            for coche in response.data:
                vehiculo = Vehiculo(
                    modelo=coche["nombre"],
                    url_modelo=str(coche["nombre"]).replace(" ", "-"),
                    imagen_public_url=self.imagen_preview(coche["imagen"]),
                    precio_venta=f"{int(coche['precio_venta']):,.0f}".replace(",", "."),
                    precio_financiado=f"{int(coche['precio_financiado']):,.0f}".replace(",", "."),
                    coches_punto_net=self.validar_campo(coche["coches_punto_net"]),
                    milanuncios=self.validar_campo(coche["milanuncios"]),
                    anio=self.validar_campo(coche["anio"]),
                    tipo=self.validar_campo(coche["tipo"]),
                    combustible=self.validar_campo(coche["combustible"]),
                    transmision=self.validar_campo(coche["transmision"]),
                    kilometraje=self.validar_campo(coche["kilometraje"]),
                    caballos=self.validar_campo(coche["caballos"]),
                    cilindrada=self.validar_campo(coche["cilindrada"]),
                    puertas=self.validar_campo(coche["puertas"]),
                    color=self.validar_campo(coche["color"]),
                )

        return vehiculo

    def validar_campo(self, v, default_value="N/A"):
        return v if v not in (None, "") else default_value

    def imagen_preview(self, path: str) -> str:
        response = self.supabase.storage.from_(self.SUPABASE_BUCKET).get_public_url(path)
        return response[:-1]

    def send_form_msg(self, data: dict):
        self.supabase.table(self.SUPABASE_FORM).insert(data, default_to_null=True).execute()


# Debug on local.
if __name__ == "__main__":
    api = SupabaseAPI()
    print(api.send_form_msg({
        'motivo': 'Consulta sobre disponibilidad',
        'nombre': 'Juan',
        'apellidos': 'Pérez García',
        'email': 'juan.perez@example.com',
        'telefono': '123456789',
        'mensaje': 'Hola, estoy interesado en un vehículo. ¿Está disponible?',
        'fecha_envio': '2024-06-17',
    }))
