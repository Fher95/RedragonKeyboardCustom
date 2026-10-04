import hid

VID = 0x258A
PID = 0x0049

# 1. Cargar el Data Fragment copiado de Wireshark
config_hex = "0608c80040000000000000000000000000000000000000000000000000ff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffffff00000000ff00ff00ffff00ff00ff00ffffffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
raw_bytes = bytes.fromhex(config_hex)

# Asegurar tamaño exacto esperado por la transferencia (1032 bytes como vimos en wLength)
# Si el payload es menor o mayor a 1032, lo ajustamos
target_length = 1032
if len(raw_bytes) < target_length:
    payload = list(raw_bytes) + [0x00] * (target_length - len(raw_bytes))
else:
    payload = list(raw_bytes[:target_length])

print(f"Longitud del payload a enviar: {len(payload)} bytes")

# 2. Iterar por TODAS las colecciones Vendor Defined (0xff00)
vendor_devices = [
    dev for dev in hid.enumerate(VID, PID) 
    if dev['usage_page'] == 0xff00
]

print(f"Se encontraron {len(vendor_devices)} colecciones Vendor Defined.")

exito = False
for dev_info in vendor_devices:
    path = dev_info['path']
    print(f"\nProbando en Path: {path}")
    
    d = hid.device()
    try:
        d.open_path(path)
        
        # Probar envío de Feature Report
        bytes_sent = d.send_feature_report(payload)
        
        if bytes_sent >= 0:
            print(f"--> ¡ÉXITO! Se enviaron {bytes_sent} bytes en este path.")
            exito = True
            d.close()
            break
        else:
            print("--> Error -1: Rechazado por el sistema en este path.")
    except Exception as e:
        print(f"--> Excepción: {e}")
    finally:
        try:
            d.close()
        except:
            pass

if not exito:
    print("\nNinguna colección aceptó el paquete de 1032 bytes.")
