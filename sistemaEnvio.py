#DECLARAR VARIABLES---------------------------------------------------------------- 
cantidad_productos = int(input("\n\nCaptura la cantidad de productos: "))
lista_productos = []

#CICLO PARA LLENAR LA LISTA DE PRODUCTOS-------------------------------------------
for i in range(cantidad_productos):
    print(f" \nProducto {i + 1}")

    nombre_producto = input("Registra el NOMBRE del producto:  ")
    caducidadDias = int(input("Registra la CADUCIDAD en dias: "))

#LISTA DE LAS PROPIEDADES DEL PRODUCTO---------------------------------------------
    producto = {
        "nombre": nombre_producto,
        "caducidad": caducidadDias
    }

#EL MÉTODO append() AGREGA EL PRODUCTO A LA LISTA DE PRODUCTOS.--------------------
    lista_productos.append(producto)

#EL MÉTODO sort() ORDENA LISTAS EN PYTHON------------------------------------------
lista_productos.sort(key = lambda producto: producto["caducidad"])

print("\n<< PLAN DE ENVÍO PRIORITARIO - G17 - Grupo1 - [EJPG] >>")
#CICLO PARA IMPRIMIR LA LISTA DE PRODUCTOS-----------------------------------------
for i, producto in enumerate(lista_productos, start=1):
    print(f"{i}) {producto['nombre']} \t- {producto['caducidad']} días")