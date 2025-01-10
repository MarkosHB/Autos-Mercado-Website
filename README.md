# Autos Mercado, su concesionario particular de confianza.

Bienvenido al repositorio que aloja la página web del concesionario Autos Mercado, localizado en Vélez-Málaga y con un amplio recorrido en el sector. Aquí encontrará los recursos elaborados para el despliegue en producción de la web-catálogo con sus vehículos y servicios disponibles.

## Desglose de las tecnologías empleadas.
- ### Frontend:
  **[Reflex](https://reflex.dev/)**, el framework de código abierto para crear e implementar aplicaciones web completamente en Python.
  
- ### Backend:
  **[Django](https://www.djangoproject.com/)**, como panel de administración para poblar de datos la web-catálogo (no disponible en este repositorio).
  
  **[Supabase](https://supabase.com/)**, empleando la API de Python con el fin de establecer las comumicaciones entre la base de datos y la web.   
  
- ### Despliegue a producción:
  **[Vercel](https://vercel.com/)**, donde se alojan los recursos estáticos elaborados generados por reflex disponibles en `public/`.
  
  **[Railway](https://railway.com/)**, para desplegar el contenedor Docker con la lógica de la página definida mediante funciones Python. 
