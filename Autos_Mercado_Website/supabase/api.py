from Autos_Mercado_Website.supabase.vehiculo import Vehiculo
from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()


async def coches_info() -> list[Vehiculo]:
    return SUPABASE_API.fetch_data()
