# Servidor de Análisis Emocional

Este proyecto utiliza **Flask** y **TensorFlow** para analizar emociones en videos. El modelo de machine learning procesa los videos y devuelve un porcentaje de las emociones detectadas. El servidor se expone mediante una API REST que puede ser consumida por aplicaciones móviles o web.

## Funcionalidades

- **Análisis de emociones**: Detecta emociones a partir de videos subidos.
- **API REST**: Exposición de la funcionalidad a través de una API.
- **Docker**: El proyecto incluye un `Dockerfile` para facilitar el despliegue. (Unconfigured)

## Prerrequisitos

Antes de comenzar, asegúrate de tener los siguientes requisitos:

- **Node.js**: Necesario para instalar LocalTunnel.
- **LocalTunnel**: Utilizado para exponer la API a través de una URL pública.

### Instalación de LocalTunnel
1. Instala Node.js desde [aquí](https://nodejs.org/) si aún no lo tienes.
2. Luego, instala LocalTunnel globalmente con el siguiente comando:
   ```bash
   npm install -g localtunnel

## Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/JeanDev11/Servidor-AnalisisEmocional.git

2. **Crear un entorno virtual**
   Es recomendable usar Python 3.10.11
   
4. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt

5. **Inicia el servidor Flask**
   ```bash
   python start_server.py

## Uso
La API se expone en una URL pública proporcionada por LocalTunnel.

## Endpoints
POST /upload_video: Permite subir un video para analizar las emociones.

### Request Body
Envía un archivo de video en el cuerpo de la solicitud.
```bash
curl -X POST https://your-localtunnel-url/upload_video \
  -F "video=@/path/to/your/video.mp4"
```

### Respuesta
El servidor responderá con un JSON que contiene los porcentajes de emociones detectadas en el video.
```bash
{
  "Disgustado": 0.00028,
  "Enojado": 0.00026,
  "Feliz": 0.98078,
  "Miedo": 0.00016,
  "Neutral": 0.01650,
  "Sorpresa": 0.00124,
  "Triste": 0.00075
}
```

## Licencia
Este proyecto está licenciado bajo la MIT License.
