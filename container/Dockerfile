# Usa una imagen base de Python
FROM python:3.9-slim

LABEL maintainer="Tu Nombre <tuemail@ejemplo.com>"
# LABEL version="1.0"
LABEL description="Dockerfile de prueba."
# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY main.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crea los directorios necesarios
RUN mkdir inbox outbox

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
