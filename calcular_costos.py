from config import *

def calcular_costos(cemento_t, asfalto_t, grava_t, acero_kg, volumen_m3):
    costo_cement = cemento_t * PRECIO_CEMENTO_TON
    costo_asfalto = asfalto_t * PRECIO_ASFALTO_TON
    costo_grava = grava_t * PRECIO_GRAVA_TON
    costo_acero = acero_kg * PRECIO_ACERO_REF_KG
    costo_mano = volumen_m3 * COSTO_MANO_OBRA_PAVIMENTO
    costo_maq = volumen_m3 * COSTO_MAQUINARIA_PAVIMENTO
    total = costo_cement + costo_asfalto + costo_grava + costo_acero + costo_mano + costo_maq
    return costo_cement, costo_asfalto, costo_grava, costo_acero, costo_mano, costo_maq, total
