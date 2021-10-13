"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
import time
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Las n obras más antiguas para un medio específico")
    print('3- Las n obras de una nacionalidad específica')
    print("4- ")
    print('5- Salir')

catalog = None

def printOlderArtworksByMedium(older_medium_artworks):
    for artwork in lt.iterator(older_medium_artworks):
        print('Título: ' + artwork['Title'] + ', Fecha de creación: ' + artwork['Date'] + 
                ', Medio '+ artwork['Medium'] + ', Dimensiones: ' + artwork['Dimensions'])

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        start_time = time.process_time()
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        controller.loadData(catalog)
        print('Obras cargadas: ' + str(controller.artworksSize(catalog)))
        print('Artistas cargados: ' + str(controller.artistsSize(catalog)))
        print('Técnicas registradas: ' + str(controller.mediumsSize(catalog)))
        print('Nacionalidades registradas: ' + str(controller.nationalitiesSize(catalog)))
        stop_time = time.process_time()
        elapsed_time_mseg = elapsed_time_mseg = (stop_time - start_time)*1000  
        print('Los datos tardaron:', elapsed_time_mseg, 'mseg en cargar.' )

    elif int(inputs[0]) == 2:
        medium = input('Ingrese el medio: ')
        num_artworks = int(input('Ingrese el número de obras más antiguas que desea ver: '))
        older_medium_artworks = controller.getOlderArtworksByMedium(catalog, medium, num_artworks)
        printOlderArtworksByMedium(older_medium_artworks)
    elif int(inputs[0]) == 3:
        nationality = input('Ingrese la nacionalidad: ')
        #num_artworks =int(input('Ingrese el número de obras de la nacionalidad que desea ver: '))
        num_artworks = 10
        nationality_artworks = controller.getArtworksByNationality(catalog, nationality, num_artworks)
        print('Existen', nationality_artworks[1], 'obras de arte de la nacionalidad indicada')
    else:
        sys.exit(0)
sys.exit(0)