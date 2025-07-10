opcion = 0
estado = True

lista_producto = [
    {"modelo":"8475HD","marca":"HD","pantalla":15.6,"RAM":"8GB","disco":"DD","GB_de_DD":"IT","procesador":"Intel_Core_i5","video":"Nvidia_GTX1050"},
    {"modelo":"2175HD","marca":"lenovo","pantalla":14,"RAM":"4GB","disco":"SSD","GB_de_DD":"512GB","procesador":"Intel_Core_i5","video":"Nvidia_GTX1050"}
]

lista_stock = [
    {"modelo":"8475HD",
     "precio":299000,
     "stock":1},
    {"modelo":"2175HD",
     "precio":39900,
     "stock":1}
]

lista_producto.append(lista_stock)



def stock_marca():
    marca_a_consultar = input("ingrese una marca a buscar: ")
    encontrado = False
    for stock in (lista_producto):
        if stock['marca'] == marca_a_consultar:
            print(f"el stock es:{"stock"}")
            encontrado = True
            break
    if not encontrado:
        print("el stock es:0")
    print("----------------------------")


def busqueda_precio():
    precio_minimo = input("ingrese precio minimo")
    precio_maximo = input("ingrese precio maximo")
    for p in lista_producto:
        if p("precio") > precio_minimo and p("precio" < precio_maximo):
            print(f"los notebook entre los precios son{p[lista_producto]}")


def actualizar_precio():
    modelo_buscado = input("ingrese modelo a actualizar")
    encontrado = False
    for modelo in lista_producto:
        if modelo('modelo') == modelo_buscado:
            precio_nuevo = input("ingrese precio nuevo")
            for p, precio in enumerate(lista_producto):
                if precio['precio'] < precio_nuevo or precio["precio"] > precio_nuevo:
                    lista_producto.pop(p)
                    lista_producto.append = {"precio":precio_nuevo,}
                    print("precio actualizado")


    if not encontrado:
        print("el modelo no existe")
    print("-----------------------------")


while estado:

    print("1) stock marca.")
    print("2) busqueda precio")
    print("3) actualizar precio")
    print("4) salir")
    opcion = int(input("selecione una opcion: "))






    if opcion == 1:
       stock_marca()



    if opcion == 2:
        busqueda_precio()


    if opcion == 3:
        actualizar_precio()


    if opcion == 4:
        print("saliendo del programa...")
        estado = False





   
       