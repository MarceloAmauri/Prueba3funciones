import json

def EditarCategoria(categoria:str):
    with open('biblioteca.json', mode='r') as ArchivoJson:
        datos = json.load(ArchivoJson)
        for i in len(ArchivoJson["Categoria"]):
            print()

    with open('biblioteca.json', mode='w') as ArchivoJson:
        json.dump(datos,ArchivoJson,indent=4)

def BuscarCategoria(categoriaID:int):
    with open('biblioteca.json', mode='r') as ArchivoJson:
        datos=json.load(ArchivoJson)
        print(ArchivoJson["Categoria"])

def AgregarCategoria(nombre:int,Categoria:str):
    with open('biblioteca.json') as ArchivoJson:
        datos=json.load(ArchivoJson)
        categorias=datos['CategoriaID','Nombre']
        Categoria={
            "CategoriaID":len(datos[Categoria])+1,
            "Nombre":nombre

        }
    datos["Categoria"].append(categorias)
    with open('biblioteca.json', mode='w') as ArchivoJson:
        json.dump(datos,ArchivoJson,indent=4)

def EliminarCategoria(CategoriaID:int):
    with open('biblioteca.json', mode='r') as ArchivoJson:
        datos=json.load(ArchivoJson)
        categorias=datos["CategoriaID"]
        for categoria in [categorias]:
            if categoria['CategoriaID']==CategoriaID:
                categorias.remove(CategoriaID)
                break
    with open('biblioteca.json', mode='w') as ArchivoJson:
        json.dump(datos,ArchivoJson,indent=4)
        