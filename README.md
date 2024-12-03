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
   git clone https://github.com/Luchelo03/EmotionAnxiety_DetectionServer.git

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
El servidor responderá con un JSON que contiene las probabilidades de las emociones y el grado de ansiedad detectado en el video.
```bash
{
    "anxiety_level": "medio",
    "emotions": {
        "Disgustado": 0.07337517254750862,
        "Enojado": 0.008421605015759712,
        "Feliz": 0.004282982257680946,
        "Miedo": 0.04533363842346321,
        "Neutral": 0.36616330761810606,
        "Sorpresa": 0.25069469857088367,
        "Triste": 0.2517285991947506
    }
}
```

## Licencia
Este proyecto está licenciado bajo la MIT License.
