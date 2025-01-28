import reflex as rx
from autosmercado.supabase.api import obtener_fotos_presentacion

class PresentationState(rx.State):
    fotos_presentacion : list = []
    current_image_idx: int = 0
    interval: int = 7000 # 7 segundos
        
    @rx.event
    async def on_load(self):
        self.fotos_presentacion = await obtener_fotos_presentacion()

    @rx.event
    def cambiar_imagen(self):
        self.current_image_idx = (self.current_image_idx + 1) % len(self.fotos_presentacion)  # Error ignored
            