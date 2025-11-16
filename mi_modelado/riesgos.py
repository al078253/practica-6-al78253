def riesgos_geotecnicos(tipo_suelo, cemento_t, asfalto_t, grava_t, acero_kg):
    probs = []
    if tipo_suelo == "Arcilloso":
        probs.append("Arcilla expansiva: hinchamiento, fisuras.")
        probs.append("Asentamiento si no se compacta bien.")
    elif tipo_suelo == "Rocoso":
        probs.append("Rocas inestables: fragmentación al compactar.")
    else:
        probs.append("Suelos arenosos: baja cohesión; riesgo de licuefacción.")
        probs.append("Erosión si no hay drenaje adecuado.")

    if cemento_t > 50:
        probs.append("Muchas toneladas de cemento: riesgo de retracción y fisuración en concreto.")
    if asfalto_t > 100:
        probs.append("Gran cantidad de asfalto: más oxidación y envejecimiento sin buen sellado.")
    if grava_t > 100:
        probs.append("Alta grava: posible asentamiento si no se compacta correctamente.")
    if acero_kg > 0:
        probs.append(f"Refuerzo de acero ({acero_kg:.1f} kg): riesgo de corrosión si no se protege adecuadamente.")
        if acero_kg / (cemento_t*1000 + grava_t*1000) > 0.15:
            probs.append("Relación acero/material muy alta: puede provocar agrietamiento por excesiva rigidez.")

    return probs

def calcular_terraceria(volumen_m3, tipo_suelo):
    factor = {"Arcilloso": 1.2, "Rocoso": 0.9, "Sabloso": 1.0}.get(tipo_suelo, 1.0)
    corte = volumen_m3 * factor * 0.6
    relleno = volumen_m3 * factor * 0.4
    return corte, relleno

def calcular_drenaje(largo, ancho):
    return 2 * (largo + ancho) * 0.1
