import reflex as rx
import os
import dotenv

dotenv.load_dotenv()

config = rx.Config(
    app_name="autosmercado",
    api_url=os.getenv('RAILWAY_API_URL'),
    cors_allowed_origins=[
         "http://localhost:3000",
         "https://autos-mercado-website.vercel.app"
    ],
    theme=rx.theme(appearance="dark"),
)
