import yt_dlp

def descargar_video(url):
    try:
        # Configuración básica para descargar el video
        ydl_opts = {'format': 'best'}
        
        # Descarga el video con yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Descarga completa!")

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

# URL del video de YouTube
url_video = input("Introduce la URL del video de YouTube: ")

# Llamar a la función para descargar el video
descargar_video(url_video)