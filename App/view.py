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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf

###########################################################################################
#Funciones de exposición de resultados
###########################################################################################

def printRequirement1(requirement_list):
    requirement_info = controller.requirement1Info(requirement_list)
    num_artists = requirement_info[0]
    first_artists = requirement_info[1]
    last_artists = requirement_info[2]
    print('Existen', num_artists, 'artistas nacidos en el rango de fechas indicado')
    print('')
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

def printRequirement2(requirement_list, num_purchased_artworks, catalog):
    requirement_info = controller.requirement2Info(requirement_list)
    num_artworks = requirement_info[0]
    first_artworks = requirement_info[1]
    last_artworks = requirement_info[2]
    print('Existen', num_artworks, 'obras de arte adquiridas en el rango de fechas indicado')
    print('Existen', num_purchased_artworks, 'obras de arte adquiridas por compra en el rango de fechas indicado')
    print('')
    print('Las primeras 3 obras de arte del rango de fechas son:')
    for artwork in lt.iterator(first_artworks):
        authors = ''
        for author_Id in controller.GetConstituentIDList(artwork['ConstituentID']):
            author_name = me.getValue(mp.get(catalog['artists_Ids'], author_Id))['info']['DisplayName']
            authors += ' ,' + author_name
        authors = authors[2:]
        print('Título: ' + artwork['Title'] + ', Artista(s): ' +  authors + 
                    ', Fecha de adquisición: ' + artwork['DateAcquired'] + ', Medio '+ artwork['Medium'] + 
                    ', Dimensiones: ' + artwork['Dimensions'])
    print('')
    print('Las últimas 3 obras de arte del rango de fechas son:')
    for artwork in lt.iterator(last_artworks):
        authors = ''
        for author_Id in controller.GetConstituentIDList(artwork['ConstituentID']):
            author_name = me.getValue(mp.get(catalog['artists_Ids'], author_Id))['info']['DisplayName']
            authors += ' ,' + author_name
        authors = authors[2:]
        print('Título: ' + artwork['Title'] + ', Artista(s): ' +  authors + 
                    ', Fecha de adquisición: ' + artwork['DateAcquired'] + ', Medio '+ artwork['Medium'] + 
                    ', Dimensiones: ' + artwork['Dimensions'])

###########################################################################################

def printRequirement3(requirement_list, num_total_artworks, name_most_used_medium):
    requirement_info = controller.requirement3Info(requirement_list)
    num_artworks_medium = requirement_info[0]
    first_artworks = requirement_info[1]
    last_artworks = requirement_info[2]
    print('Existen', num_total_artworks, 'obras de arte del artista.')
    print('Existen', num_artworks_medium, 'obras de arte del artista hechos con la técnica', name_most_used_medium, '.')
    print('')
    print('Las primeras 3 obras de arte de la técnica más utilizada por el artista son:')
    for artwork in lt.iterator(first_artworks):
        print('Título: ' + artwork['Title'] + ', Fecha de creación: ' + artwork['Date'] +
                 ', Medio '+ artwork['Medium'] + ', Dimensiones: ' + artwork['Dimensions'])
    print('')
    print('Las últimas 3 obras de arte de la técnica más utilizada por el artista son:')
    for artwork in lt.iterator(last_artworks):
        print('Título: ' + artwork['Title'] + ', Fecha de creación: ' + artwork['Date'] +
                 ', Medio '+ artwork['Medium'] + ', Dimensiones: ' + artwork['Dimensions'])

###########################################################################################
#Menu principal
###########################################################################################

def printMenu():
    print('')
    print('Bienvenido')
    print('1- Cargar información en el catálogo')
    print('2- REQ. 1: listar cronológicamente los artistas')
    print('3- REQ. 2: listar cronológicamente las adquisiciones')
    print('4- REQ. 3: clasificar las obras de un artista por técnica')
    print('0- Salir')

###########################################################################################

def SortingAlgorithmOptions():
    print('Algoritmos de ordenamiento disponibles: ')
    print('1) Insertion Sort')
    print('2) Shell Sort')
    print('3) Merge Sort')
    print('4) Quick Sort')
    sorting_method = input('Ingrese el algoritmo elegido: ')
    return sorting_method

###########################################################################################

catalog = None

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
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
        catalog = controller.initCatalog(data_structure)
        controller.loadData(catalog, data_structure, artists_sample_size, artworks_sample_size)

    elif int(inputs[0]) == 2:
        initial_birth_year = int(input('Ingrese el primer año del intervalo: '))
        end_birth_year = int(input('Ingrese el último año del intervalo: '))
        print('Procesando...')
        requirement_info = controller.getArtistsByBirthYear(catalog, data_structure,
                                                            initial_birth_year, end_birth_year)
        elapsed_time = requirement_info[0]
        print('')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('')
        requirement_list = requirement_info[1]
        printRequirement1(requirement_list)

    elif int(inputs[0]) == 3:
        initial_adquisiton_date = input('Ingrese la primera fecha del intervalo: ')
        end_adquisition_date = input('Ingrese la última fecha del intervalo: ')
        print('')
        sorting_method = SortingAlgorithmOptions()
        print('Procesando...')
        requirement_info = controller.getArtworksByAdquisitonDate(catalog, data_structure, sorting_method,
                                                    initial_adquisiton_date, end_adquisition_date)
        elapsed_time = requirement_info[0]
        print('')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('')
        requirement_list = requirement_info[1]    
        num_purchased_artworks = requirement_info[2]                         
        printRequirement2(requirement_list, num_purchased_artworks, catalog)

    elif int(inputs[0]) == 4:
        artist_name = input('Ingrese el nombre del artista: ')
        print('')
        print('Procesando...')
        requirement_info = controller.getArtworksByMediumAndArtist(catalog, artist_name)
        elapsed_time = requirement_info[0]
        print('')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('')
        requirement_list = requirement_info[1]
        num_total_artworks = requirement_info[2]
        name_most_used_medium = requirement_info[3]
        printRequirement3(requirement_list, num_total_artworks, name_most_used_medium)

    else:
        sys.exit(0)
sys.exit(0)

