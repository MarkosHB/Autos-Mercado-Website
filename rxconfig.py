import reflex as rx

config = rx.Config(
    app_name="autosmercado",
    api_url="https://autos-mercado-website-production.up.railway.app",
    cors_allowed_origins=[
         "http://localhost"
         "https://autos-mercado-website.vercel.app"
    ]
)
