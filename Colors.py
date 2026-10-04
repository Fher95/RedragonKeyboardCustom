def establecer_color_global(payload_list, r, g, b):
    # Modificamos directamente la posición RGB descubierta
    payload_list[29] = r  # Rojo
    payload_list[30] = g  # Verde
    payload_list[31] = b  # Azul
    return payload_list

# Ejemplo: Cambiar a VERDE PURO (R:0, G:255, B:0)
payload_modificado = preparar_payload(hex_2841, 1032)
payload_modificado = establecer_color_global(payload_modificado, 0x00, 0xFF, 0x00)

# Al enviar la secuencia con payload_modificado, ¡el teclado se pondrá verde!