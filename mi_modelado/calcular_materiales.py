from config import *

def calcular_materiales(largo, ancho, espesor_cm, tipo_pavimento):
    espesor_m = espesor_cm / 100
    volumen_m3 = largo * ancho * espesor_m
    densidad_promedio = 2.3  # t/m3

    toneladas = volumen_m3 * densidad_promedio

    if tipo_pavimento == "Asfalto":
        cemento_t, asfalto_t, grava_t, acero_kg = 0, toneladas, 0, 0
    elif tipo_pavimento == "Concreto":
        cemento_t = toneladas * 0.3
        asfalto_t = 0
        grava_t = toneladas * 0.6
        acero_kg = 120 * volumen_m3  # kg
    else:  # Mixto
        cemento_t = toneladas * 0.15
        asfalto_t = toneladas * 0.6
        grava_t = toneladas * 0.25
        acero_kg = 0

    return volumen_m3, cemento_t, asfalto_t, grava_t, acero_kg
