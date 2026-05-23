from pathlib import Path
from PIL import Image



def redimensionar_y_guardar(
    carpeta_entrada: str,
    carpeta_salida_base: str = "datasets",
    size: tuple[int, int] = (128, 128),
) -> None:
    entrada_path = Path(carpeta_entrada)
    salida_path = Path(carpeta_salida_base) / entrada_path.name

    for clase in ["normal", "pneumonia"]:
        origen_clase = entrada_path / clase
        destino_clase = salida_path / clase
        destino_clase.mkdir(parents=True, exist_ok=True)

        if not origen_clase.exists():
            print(f"No existe la carpeta: {origen_clase}")
            continue

        for archivo in origen_clase.iterdir():
            if not archivo.is_file():
                continue

            if archivo.suffix.lower() not in {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}:
                continue

            try:
                with Image.open(archivo) as img:
                    img_redimensionada = img.resize(size, Image.Resampling.LANCZOS)
                    img_redimensionada.save(destino_clase / archivo.name)
            except Exception as e:
                print(f"No se pudo procesar {archivo}: {e}")

    print(f"Imágenes procesadas en: {salida_path.resolve()}")


def procesar_carpetas_raiz() -> None:
    for carpeta in ["train", "test","validation"]:
        redimensionar_y_guardar(carpeta_entrada=carpeta)


if __name__ == "__main__":
    procesar_carpetas_raiz()