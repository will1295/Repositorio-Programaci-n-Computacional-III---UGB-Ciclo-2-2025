from collections import defaultdict

precios = {"manzana":1.5,"guineo":0.45}

print(precios.get("manzana",0.0))
print(precios.get("guineo"),0.0)

inventario = defaultdict(int)

inventario["manzana"] += 5
print(inventario["manzana"])
print(inventario["guineo"])