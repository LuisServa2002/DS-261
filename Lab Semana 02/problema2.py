# Leer N (socios), M (terminales), S (transacciones)
N, M, S = map(int, input().split())

# Diccionario: terminal -> socio
terminal_socio = {}
for _ in range(M):
    p, t = map(int, input().split())
    terminal_socio[t] = p #Almacena en el diccionario terminal(llave)-socio(valor) 

print(terminal_socio)

# Diccionario: (socio, cliente) -> cantidad de compras
compras = {}
for _ in range(S):
    c, t = map(int, input().split())
    
    # Si el terminal no pertenece a ningún socio, ignorar
    if t not in terminal_socio:
        continue
    
    socio = terminal_socio[t]
    
    # Si es la primera compra de este cliente en este socio, iniciar en 0
    if (socio, c) not in compras: #id socio-id cliente
        compras[(socio, c)] = 0
    
    compras[(socio, c)] += 1
    
print(compras)

# Para cada socio, buscar su cliente más fiel
for socio in range(1, N + 1):
    mejor_cliente = -1
    mejor_cantidad = 0
    
    # Revisar todos los pares (socio, cliente) que existen
    for (s, c), cantidad in compras.items():
        if s != socio:
            continue
        
        # Actualizar si tiene más compras, o igual cantidad pero menor ID
        if cantidad > mejor_cantidad:
            mejor_cantidad = cantidad
            mejor_cliente = c
        elif cantidad == mejor_cantidad and c < mejor_cliente:
            mejor_cliente = c
    
    print(socio, mejor_cliente)