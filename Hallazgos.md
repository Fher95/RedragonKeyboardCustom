[Handshake] Col05 (6 bytes)   -> Desbloquea la interfaz
[Bloque 0]   Col06 (1032 B)    -> Carga RGB Global y Teclas (06 00...)
[Bloque 1]   Col06 (1032 B)    -> Carga Máscaras de LED/Mapeo (06 01...)
[Bloque 2]   Col06 (1032 B)    -> Carga Datos de Macros/Estado (06 02...)
[Commit]     Col06 (1032 B)    -> Orden de Aplicar y Guardar (06 03...) (CONFIGURACION DE EFECTO)



COLORES:

En la primera llamada de 1032 bytes, se encontró que del offset 29 al 31 se settea el valor correspondiente al color (r,g,b) en hexa

Longitud B1: 1032 bytes | Longitud B2: 1032 bytes

Offset (Decimal)   | Offset (Hex)   | Valor A (Hex)  | Valor B (Hex)
-----------------------------------------------------------------
29                 | 0x001D         | 0xFF           | 0x00
31                 | 0x001F         | 0x00           | 0xFF
-----------------------------------------------------------------
Total de bytes diferentes: 2


EFECTOS:

Se configuran en la cuarta llamada de 1032 bytes, en el offset 21 (0x0015), aqui un ejemplo del efecto Respire (0x02) comparado con un efecto de color estatico (0x01)

Longitud B1: 1032 bytes | Longitud B2: 1032 bytes

Offset (Decimal)   | Offset (Hex)   | Valor A (Hex)  | Valor B (Hex)
-----------------------------------------------------------------
21                 | 0x0015         | 0x02           | 0x01
-----------------------------------------------------------------
Total de bytes diferentes: 1