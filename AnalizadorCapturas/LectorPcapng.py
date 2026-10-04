from pyshark import FileCapture


def extraer_data_fragments(ruta_pcapng: str) -> dict[int, str | None]:
    """Extrae usb.data_fragment de las filas 0, 2, 3, 4 y 5 del archivo."""
    filas = (0, 2, 3, 4, 5)
    fragmentos: dict[int, str | None] = {fila: None for fila in filas}
    captura = FileCapture(ruta_pcapng)
    try:
        for indice, paquete in enumerate(captura):
            if indice in fragmentos:
                data = getattr(paquete, "data", None)
                data_fragment = getattr(data, "usb_data_fragment", None)
                data_fragment = data_fragment.replace(':','') if data_fragment != None else data_fragment
                fragmentos[indice] = data_fragment
            if indice == filas[-1]:
                break
    finally:
        captura.close()

    return fragmentos

if __name__ == "__main__":
    resultado = extraer_data_fragments("./Capturas/Rainbow.pcapng")
    print(resultado)
    