# Usar una imagen base de Python
FROM python:3.10.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libgl1 \
    && apt-get clean

# Crear directorio de trabajo
WORKDIR /app

# Copiar el código de la aplicación
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
