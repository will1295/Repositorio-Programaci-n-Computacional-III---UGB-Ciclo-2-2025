def calcular_totales(cliente,descuento):
    totales = {}
    for cliente, compras in cliente.items():
        total = 0
        for producto, info in compras.items():
            precio = info["precio"]
            cantidad = info["cantidad"]
            if info["descuento"]:
                precio = precio -(precio * descuento)
            total += precio * cantidad
        totales[cliente] = total
    return totales

clientes = {
    "Ana":{"laptop":{"precio":1000,"cantidad":1,"descuento":True}}
}

print(calcular_totales(clientes,0.20))