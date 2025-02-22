import os
import dotenv
from supabase import create_client, Client
from autosmercado.supabase.vehiculo import Vehiculo
from autosmercado.utils import MAX_FORM_MSGs


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
            .select("id, nombre, imagen, precio_venta, precio_financiado, coches_punto_net, milanuncios, anio, tipo, "
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
                    fotos=self.obtener_fotos(coche["id"], self.imagen_preview(coche["imagen"])),
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
    
    def fetch_presentation_photos(self) -> list[str]:
        response = (
            self.supabase.table(self.SUPABASE_TABLE)
            .select("imagen, id")
            .filter('check_anunciado', 'eq', True)
            .filter('check_vendido', 'eq', False)
            .execute()
        )

        fotos = []

        if len(response.data) > 0:
            for coche in response.data:
                fotos.extend(self.obtener_fotos(coche["id"], self.imagen_preview(coche["imagen"])))

        return fotos


    def validar_campo(self, v, default_value="N/A"):
        return v if v not in (None, "") else default_value

    def imagen_preview(self, path: str) -> str:
        return self.supabase.storage.from_(self.SUPABASE_BUCKET).get_public_url(path)
    
    def obtener_fotos(self, iden: str, foto_principal: str) -> list:
        response = (self.supabase.storage.from_(self.SUPABASE_BUCKET).list(path=f"Stock/{iden}"))

        fotos = [foto_principal]
        for item in response:
            fotos.insert(1, self.imagen_preview(f"Stock/{iden}/{item['name']}"))

        return fotos

    def send_form_msg(self, data: dict) -> bool:
        response = self.supabase.table(self.SUPABASE_FORM).select("id", count="exact").execute()
        if response.count <= MAX_FORM_MSGs:
            self.supabase.table(self.SUPABASE_FORM).insert(data, default_to_null=True).execute()
        return response.count <= MAX_FORM_MSGs


# Debug on local.
if __name__ == "__main__":
    api = SupabaseAPI()
