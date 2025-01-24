import reflex as rx
import os
import dotenv

dotenv.load_dotenv()
RAILWAY_API_URL = os.getenv('RAILWAY_API_URL')

config = rx.Config(
    app_name="autosmercado",
    # api_url=RAILWAY_API_URL,
    cors_allowed_origins=[
         "http://localhost:3000",
         "https://autos-mercado.vercel.app"
    ],
    theme=rx.theme(appearance="dark"),
)
