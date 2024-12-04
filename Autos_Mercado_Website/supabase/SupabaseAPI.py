import os
import dotenv
from supabase import create_client, Client
from Autos_Mercado_Website.supabase.vehiculo import Vehiculo


class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    def fetch_data(self):
        response = self.supabase.table("stock_coche").select("*").execute()
        print(response)
        vehiculo_data = []

        if len(response.data) > 0:
            for coche in response.data:
                vehiculo_data.append(
                    Vehiculo(
                        modelo=coche["nombre"],
                    )
                )

        return vehiculo_data
