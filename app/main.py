from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    """
    Crea un archivo de log cada segundo en el directorio actual,
    nombrado con la hora actual y conteniendo el timestamp.
    """
    print("Log generator started. Press Ctrl+C to stop.")

    try:
        while True:
            # 1. Obtener el tiempo actual
            now = datetime.now()

            # 2. Formatear el nombre del archivo: app-{hours}_{minutes}_{seconds}.log
            # Nota: Usamos %-H, %-M, %-S si queremos evitar ceros a la izquierda, 
            # pero el formato estándar compatible es %H_%M_%S.
            file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

            # 3. Formatear el contenido (Timestamp completo)
            timestamp_content = now.strftime("%Y-%m-%d %H:%M:%S")

            # 4. Crear y escribir el archivo
            with open(file_name, mode="w", encoding="utf-8") as f:
                f.write(timestamp_content)

            # 5. Imprimir confirmación en consola
            print(f"{timestamp_content} {file_name}")

            # 6. Esperar 1 segundo antes de la siguiente iteración
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProcess terminated by user.")


if __name__ == "__main__":
    main()
