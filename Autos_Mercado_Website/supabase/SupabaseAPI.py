import os
import dotenv
from supabase import create_client, Client
from Autos_Mercado_Website.supabase.vehiculo import Vehiculo


class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    SUPABASE_TABLE = os.environ.get("SUPABASE_TABLE")
    SUPABASE_BUCKET = os.environ.get("SUPABASE_BUCKET")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    def fetch_data(self):
        response = self.supabase.table(self.SUPABASE_TABLE).select("*").execute()

        vehiculo_data = []

        if len(response.data) > 0:
            for coche in response.data:
                vehiculo_data.append(
                    Vehiculo(
                        modelo=coche["nombre"],
                        url_modelo=str(coche["nombre"]).replace(" ", "_"),
                        imagen_public_url=self.imagen_preview(coche["imagen"]),
                    )
                )

        return vehiculo_data

    def imagen_preview(self, path: str) -> str:
        response = self.supabase.storage.from_(self.SUPABASE_BUCKET).get_public_url(path)
        return response[:-1]
