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
assert cf

###########################################################################################
#Funciones de exposición de resultados
###########################################################################################

def printRequirement1(requirement_list):
    num_artists = lt.size(requirement_list)
    first_artists = lt.subList(requirement_list, 1, 3)
    last_artists = lt.subList(requirement_list, num_artists - 3, 3)
    print('Los primeros 3 artistas del rango de años son:')
    for artist in lt.iterator(first_artists):
        print('Nombre: ' + artist['DisplayName'] + ', Año de nacimiento: ' +  artist['BeginDate'] + 
                    ', Año de fallecimiento: ' + artist['EndDate'] + ', Nacionalidad: '+ artist['Nationality'] + 
                    ', Genero: ' + artist['Gender'])
    print('')
    print('Los últimos 3 artistas del rango de años son:')
    for artist in lt.iterator(last_artists):
        print('Nombre: ' + artist['DisplayName'] + ', Año de nacimiento: ' +  artist['BeginDate'] + 
                    ', Año de fallecimiento: ' + artist['EndDate'] + ', Nacionalidad: '+ artist['Nationality'] + 
                    ', Genero: ' + artist['Gender'])

###########################################################################################
#Menu principal
###########################################################################################

def printMenu():
    print('Bienvenido')
    print('1- Cargar información en el catálogo')
    print('2- Elegir algorítmo de ordenamiento')
    print('3- REQ. 1: listar cronológicamente los artistas')
    print('4- ')
    print('0- Salir')

catalog = None

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('Existen 1948 artistas y 768 obras de arte en los archivos')
        artists_sample_size = int(input('Elija la cantidad de artistas que desea cargar: '))
        artworks_sample_size = int(input('Elija la cantidad de obras de arte que desea cargar: '))
        print('')
        print('Las estructuras de datos disponibles para cargar los datos son: ')
        print('1- Lista encadenada')
        print('2- Lista ordenada')
        data_structure = controller.getDataStructure(int(input('Elija la estructura de datos: ')))
        print("Cargando información de los archivos ...")

        initialization_results = controller.initCatalog(data_structure)
        catalog = initialization_results[2]
        loading_data_results = controller.loadData(catalog, data_structure, 
                                                    artists_sample_size, artworks_sample_size)
        total_elapsed_time = initialization_results[0] + loading_data_results[0]
        average_RAM_usage = (initialization_results[1] + loading_data_results[1])/2
        print('Información de carga: ')
        print('Tiempo empleado:', total_elapsed_time, 'mseg')
        print('Memoria RAM utilizada:', average_RAM_usage, 'porciento')

    elif int(inputs[0]) == 2:
        print('Algoritmos de ordenamiento disponibles: ')
        print('1) Insertion Sort')
        print('2) Shell Sort')
        print('3) Merge Sort')
        print('4) Quick Sort')
        sorting_method = input('Ingrese el algoritmo elegido: ')

    elif int(inputs[0]) == 3:
        initial_birth_year = int(input('Ingrese el primer año del intervalo: '))
        end_birth_year = int(input('Ingrese el último año del intervalo: '))
        print('Procesando...')
        requirement_info = controller.getArtistsByBirthYear(catalog, data_structure,
                                                            initial_birth_year, end_birth_year)
        elapsed_time = requirement_info[0]
        RAM_usage = requirement_info[1]
        print('')
        print('Información de carga: ')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('Memoria RAM utilizada:', RAM_usage, 'porciento')
        print('')
        requirement_list = requirement_info[2]
        printRequirement1(requirement_list)
    else:
        sys.exit(0)
sys.exit(0)