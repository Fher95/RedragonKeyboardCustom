from LectorPcapng import extraer_data_fragments
from HexUtils import comparar_hex

dic_primera = extraer_data_fragments('./Capturas/Rainbow.pcapng')
dic_segunda = extraer_data_fragments('./Capturas/Respire.pcapng')

for key in dic_primera.keys():
    print(f"Llamada {key}")
    comparar_hex(dic_primera[key], dic_segunda[key])
    print("")