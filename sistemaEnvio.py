#variables 
cantidad_productos = int(input("Captura la cantidad de productos por registrar: "))
lista_productos = []

#ciclo para llenar la lista de productos
for i in range(cantidad_productos):
    print(f"Producto {i + 1}")

    nombre_producto = input("Captura nombre del producto:  ")
    caducidadDias = int(input("Captura la caducidad en dias: "))

    #lista de las propiedades del producto
    producto = {
        "nombre": nombre_producto,
        "caducidad": caducidadDias
    }

    #el metodo append() agrega el producto a la lista de productos.
    lista_productos.append(producto)

# el metodo sort() ordena listas en python
lista_productos.sort( reverse= False)

# imprime lista de productos
print("\n..::<< Productos ordenados por caducidad >>::..")

for producto in lista_productos:
    print(f"Producto: {producto['nombre']} | "
          f"Días para caducar: {producto['caducidad']}")