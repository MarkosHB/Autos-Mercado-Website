from Autos_Mercado_Website.supabase.vehiculo import Vehiculo
from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()


async def coche_info() -> list[Vehiculo]:
    return SUPABASE_API.fetch_data()
