import json
import funciones
import time
import os



while True:
    print('*******************************')
    print('*         MUNDO LIBRO         *')
    print('*******************************')
    print('                               ')
    print('                               ')
    print('[1] - Mantenedor de categorias')
    print('[2] - Reportes ')
    print('[3] - Salir ')
    opc = int(input('Ingrese una opción: '))

    if opc == 1:
        print('************************')
        print('  Mantenedor Usuario    ')
        print('************************')
        print('                    ')
        print('                    ')
        print('[1] - Agregar categoria')
        print('[2] - Editar categoria')
        print('[3] - Eliminar categoria')
        print('[4] - Buscar categoria')
        print('[5] - Volver')
        mant = int(input('Ingrese una opción: '))
        if mant == 1:
            nombre=str(input('Ingrese el nombre de la categoria: '))
            funciones.AgregarCategoria(nombre)
            print('Agregado correctamente!:3 ')
            time.sleep(1)
            os.system("cls")

        if mant == 2:
            nombre=str(input('Ingrese el nombre que quiere editar: '))
            funciones.EditarCategoria(nombre)
            print('Nombre correctamente editado ^_^')
            time.sleep(1)
            os.system("cls")

        if mant ==3:
            CateogriaID=int(input('Ingresa la categoria que quieres eliminar: '))
            funciones.EliminarCategoria(CateogriaID)
            print('Eliminado Correctamente!^_^')
            time.sleep(1)
            os.system("cls")

        if mant == 4:
            print(funciones.BuscarCategoria)
            time.sleep(1)
            os.system("cls")

        if mant == 5:
            break
if opc == 2:
    print('*********************************************')
    print('*      LIBRO      CANTIDAD DE VECES PRESTADO ')
    print('*********************************************')
    print(' La casa de Bernarda Alba,'                   )
    print('La fiesta del Chivo                          ')