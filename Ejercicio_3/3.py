def orden(naves):
    ordenadas = sorted(naves, key=lambda x:(x["nombre"], x["longitud"]))
    print(f"Naves ordenadas por nombre y longitud:")
    for nave in ordenadas:
        return nave

def info(naves):
    for nave in naves:    
        if nave["nombre"].lower() == "cometa veloz":
            return f"Información de la nave 'Cometa Veloz':\n\n{nave}"
        if nave["nombre"].lower() == "titan del cosmos":
            return f"Información de la nave 'Titan del Cosmos':\n\n{nave}"

def mas_pasajeros(naves):
    return sorted(naves, key=lambda x: x["pasajeros"], reverse=True)[:5]

def mas_tripulacion(naves):
    return max(naves, key=lambda x: x["tripulantes"])

def GX(naves):
    naves_gx = []
    for nave in naves:
        if nave["nombre"].startswith("GX"):
            naves_gx.append(nave)
    print("Naves cuyo nombre comienza con GX:")
    for nave in naves_gx:
        return nave
    
def seis_pasajeros(naves):
    naves_seis_o_mas_pasajeros = []
    for nave in naves:
        if nave["pasajeros"] >= 6:
            naves_seis_o_mas_pasajeros.append(nave)
    print("Naves que pueden llevar seis o más pasajeros:")
    for nave in naves_seis_o_mas_pasajeros:
        return nave

def pequeña_y_grande(naves):
    nave_grande = max(naves, key=lambda x: x["longitud"])
    nave_pequena = min(naves, key=lambda x: x["longitud"])
    return f"Nave más grande:\n\n{nave_grande}\n\nNave más pequeña:\n\n{nave_pequena}"

naves = [
    {"nombre":"cometa veloz", "longitud":52, "tripulantes":12, "pasajeros":105},
    {"nombre":"titan del cosmos", "longitud":75, "tripulantes":18, "pasajeros":160},
    {"nombre":"GX-1", "longitud":42, "tripulantes":9, "pasajeros":65},
    {"nombre":"GX-2", "longitud":47, "tripulantes":10, "pasajeros":75},
    {"nombre":"Estrella Fugaz", "longitud":58, "tripulantes":13, "pasajeros":85},
    {"nombre":"Nebulosa", "longitud":68, "tripulantes":16, "pasajeros":95},
    {"nombre":"Galaxia", "longitud":63, "tripulantes":12, "pasajeros":115},
]

orden(naves)

print(info(naves))

print("\nCinco naves con mayor cantidad de pasajeros:")
for nave in mas_pasajeros(naves):
    print(nave)

print("\nNave que requiere la mayor cantidad de tripulación:")
print(mas_tripulacion(naves))

GX(naves)

seis_pasajeros(naves)

print(pequeña_y_grande(naves))