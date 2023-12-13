import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

opcion = 0

while opcion != 5:
    print("Seleccione una opción:")
    print("1. Grabar")
    print("2. Reproducir")
    print("3. Graficar")
    print("4. Graficar densidad")
    print("5. Salir")
    
    opcion = int(input("Ingrese su elección: "))
    
    if opcion == 1:
        try:
            duracion = float(input("Ingrese la duración de la grabación en segundos: "))
            print("Comenzando la grabación...")
            fs = 44100  # Frecuencia de muestreo
            grabacion = sd.rec(int(duracion * fs), samplerate=fs, channels=1)
            sd.wait()
            print("Grabación finalizada")
            archivo = "audio.wav"
            wav.write(archivo, fs, grabacion)  # Guardar la grabación en formato WAV
            print("Archivo de audio grabado correctamente")
        except:
            print("Error al grabar el audio")
    
    elif opcion == 2:
        try:
            fs, data = wav.read("audio.wav")
            sd.play(data, fs)
            sd.wait()
        except:
            print("Error al reproducir el audio")
    
    elif opcion == 3:
        try:
            fs, data = wav.read("audio.wav")
            tiempo = np.arange(0, len(data)) / fs
            plt.plot(tiempo, data)
            plt.xlabel("Tiempo (s)")
            plt.ylabel("Amplitud")
            plt.title("Audio")
            plt.show()
        except:
            print("Error al graficar el audio")
    
    elif opcion == 4:
        try:
            print("Graficando espectro de frecuencia...")
            fs, data = wav.read("audio.wav")
            N = len(data)
            f = np.fft.rfftfreq(N, d=1/fs)
            ventana = np.hanning(N)
            Sxx = np.abs(np.fft.rfft(data * ventana))**2
            plt.semilogy(f, 10 * np.log10(Sxx))
            plt.xlabel("Frecuencia (Hz)")
            plt.ylabel("Densidad espectral de potencia (dB/Hz)")
            plt.title("Espectro de frecuencia de señal grabada")
            plt.show()
        except:
            print("Error al graficar el espectro de frecuencia")
    
    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida")
