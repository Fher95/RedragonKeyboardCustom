from LectorPcapng import extraer_data_fragments
from HexUtils import comparar_hex

DIR_1 = './Capturas/Respire.pcapng'
DIR_2 = './Capturas/Rainbow.pcapng'
dic_primera = extraer_data_fragments(DIR_1)
dic_segunda = extraer_data_fragments(DIR_2)
print("")
print(f"Comparacion entre las capturas {DIR_1.split('/')[-1]} y {DIR_2.split('/')[-1]} (5 llamdas)")
print("")
llamadas_diferentes = []
for key in dic_primera.keys():
    print(f"Llamada {key}", end="")
    diferencias = comparar_hex(dic_primera[key], dic_segunda[key])
    if (diferencias > 0):
        llamadas_diferentes.append(key)
    else: 
        print(": Sin diferencia")
    print("")
print(f"{len(llamadas_diferentes)} llamdas diferentes: ", llamadas_diferentes)