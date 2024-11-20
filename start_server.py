import subprocess

# Configuración
FLASK_COMMAND = "python app.py"  # Comando para iniciar tu servidor Flask
LOCALTUNNEL_COMMAND = "lt --port 5000 --subdomain serveranalisisemocional"  # Comando LocalTunnel

try:
    # Inicia el servidor Flask
    print("Iniciando servidor Flask...")
    flask_process = subprocess.Popen(FLASK_COMMAND, shell=True)

    # Inicia LocalTunnel
    print("Exponiendo el servidor con LocalTunnel...")
    lt_process = subprocess.Popen(LOCALTUNNEL_COMMAND, shell=True)

    # Esperar a que el usuario detenga manualmente
    print("Servidor corriendo. Presiona Ctrl+C para detener.")
    flask_process.wait()
except KeyboardInterrupt:
    print("\nDeteniendo procesos...")
    flask_process.terminate()
    lt_process.terminate()
    flask_process.wait()
    lt_process.wait()
    print("Todos los procesos han sido detenidos.")

