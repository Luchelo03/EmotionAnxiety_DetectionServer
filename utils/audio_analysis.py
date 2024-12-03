import librosa
import numpy as np
import joblib

# Cargar el modelo de análisis de audio
audio_model_path = "models/audio_emotion_model.joblib"
audio_model = joblib.load(audio_model_path)

# Función para extraer características de un archivo de audio
def extract_audio_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13).T, axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr).T, axis=0)
    rms = np.mean(librosa.feature.rms(y=y).T, axis=0)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return np.hstack([mfcc, chroma, rms, tempo])

# Función para predecir el nivel de ansiedad basado en el audio
def predict_anxiety(audio_path):
    try:
        features = extract_audio_features(audio_path)
        features = features.reshape(1, -1)  # Redimensionar para el modelo
        anxiety_level = audio_model.predict(features)[0]
        return anxiety_level
    except Exception as e:
        print(f"Error en el análisis de audio: {e}")
        return "Error"
