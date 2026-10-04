MODOS_EFECTO = {
    "FIXED_ON": 0x01,  # Confirmado
    "RESPIRE":  0x02,  # Confirmado
    "RAINBOW":  0x03,  # Confirmado
    "FLASH_AWAY": 0x04,
    "RAINDROPS": 0x05,
    "RAINBOW_WHEEL": 0x06,
    "RIPPLES_SHINING": 0x07,
    "STARS_TWINKLE": 0x08,
    "SHADOW_DISAPPEAR": 0x09,
    "RETRO_SNAKE": 0x0A,
    "NEON_STREAM": 0x0B,
    "REACTION": 0x0C,
    "SINE_WAVE": 0x0D,
    "RETINUE_SCANNING": 0x0E,
    "ROTATING_WINDMILL": 0x0F,
    "COLORFUL_WATERFALL": 0x10,
    "BLOSSOMING": 0x11,
    "ROTATING_STORM": 0x12,
    "COLLISION": 0x13,
    "PERFECT": 0x14,
    "SELF-DEFINE": 0x15, ## Verificar el offset 20 (0x0014) que lleva un valor diferente a los demas
    "OFF": 0x00,
}
def cambiar_efecto(payload_p4, id_efecto):
    payload = list(bytes.fromhex(payload_p4))
    
    # Inyectar el ID en el offset 21 (0x0015)
    payload[21] = id_efecto
    
    return payload