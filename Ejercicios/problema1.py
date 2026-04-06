# Leer N rutas
N = int(input())

# Guardar rutas: lista de (partes_de_la_ruta, contenido)
rutas = []
for _ in range(N):
    linea = input().split()
    path = linea[0]          # Ej: /user/:id
    contenido = linea[1]     # Ej: UserPage

    partes = path.split("/") # Ej: ["", "user", ":id"]
    rutas.append((partes, contenido))
print(rutas)

# Leer M transiciones
M = int(input())

for _ in range(M):
    transicion = input().strip()                  # Ej: /user/42 (separa por espacios)
    partes_transicion = transicion.split("/")     # Ej: ["", "user", "42"] (separa por "/")
    encontrado = False

    for partes_ruta, contenido in rutas:
        # Si no tienen el mismo número de partes, no coinciden
        if len(partes_ruta) != len(partes_transicion):
            continue

        parametro = None
        coincide = True

        # Comparar parte por parte
        for r, t in zip(partes_ruta, partes_transicion):
            if r.startswith(":"):
                # Es un parámetro, guardar su valor
                parametro = t
            elif r != t:
                # No coincide exactamente
                coincide = False
                break

        if coincide:
            # Imprimir contenido y el parámetro si existe
            if parametro:
                print(contenido, parametro)
            else:
                print(contenido)
            encontrado = True
            break

    if not encontrado:
        print("404 Not Found")