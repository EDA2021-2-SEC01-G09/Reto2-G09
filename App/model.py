"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from typing import Counter
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf
###########################################################################################
# Construccion de modelos
###########################################################################################

def newCatalog(data_structure):

    catalog = {'artists_keys': None,
               'artists': None,
               'artworks': None,
               'birth_years': None,
               'adquisition_years': None,
               'nationalities': None,
               'nationalities_keys': None,
               'departments': None}
 
    catalog['artists_keys'] = lt.newList(data_structure)
    catalog['artists'] = mp.newMap(3907,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    catalog['artworks'] = mp.newMap(1543,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    catalog ['birth_years'] = mp.newMap(367,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    catalog['adquisition_years'] = mp.newMap(173,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    catalog['nationalities'] = mp.newMap(127,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    catalog['nationalities_keys'] = lt.newList(data_structure)
    catalog['departments'] = mp.newMap(17,
                                   maptype='PROBING',
                                   loadfactor=0.5)

    return catalog

###########################################################################################
# Funciones para agregar informacion al catalogo
###########################################################################################

def addArtist(catalog, artist, data_structure):
    lt.addLast(catalog['artists_keys'], artist['ConstituentID'])
    artist_info = newArtist(artist, data_structure)
    mp.put(catalog['artists'], artist['ConstituentID'], artist_info)

###########################################################################################

def addArtwork(catalog, artwork):
    mp.put(catalog['artworks'], artwork['ObjectID'], artwork)

###########################################################################################

def addBirthYearArtist(catalog, artist, data_structure):
    birth_years_map = catalog['birth_years']
    birth_year = artist['BeginDate']
    if mp.contains(birth_years_map, birth_year):
        lt.addLast(me.getValue(mp.get(birth_years_map, birth_year)), artist)
    else:
        birth_year_list = lt.newList(data_structure)
        lt.addLast(birth_year_list, artist)
        mp.put(birth_years_map, birth_year, birth_year_list)

###########################################################################################

def addAdquisitionYear(catalog, artwork, data_structure):
    adquisition_years_map = catalog['adquisition_years']
    adquisition_year = getAdquisitionYear(artwork['DateAcquired'])

    if mp.contains(adquisition_years_map, adquisition_year):
        lt.addLast(me.getValue(mp.get(adquisition_years_map, adquisition_year)), artwork)
    else:
        adquisition_year_list = lt.newList(data_structure)
        lt.addLast(adquisition_year_list, artwork)
        mp.put(adquisition_years_map, adquisition_year, adquisition_year_list)

###########################################################################################

def addMedium(catalog, artwork, data_structure):
    artists_Ids_list = GetConstituentIDList(artwork['ConstituentID'])
    medium = artwork['Medium']
    for artist_Ids in artists_Ids_list:
        artist_mediums = me.getValue(mp.get(catalog['artists'], artist_Ids))['mediums']
        if mp.contains(artist_mediums, medium):
            lt.addLast(me.getValue(mp.get(artist_mediums, medium)), artwork)
        else:
            medium_artworks_list = lt.newList(data_structure)
            lt.addLast(medium_artworks_list, artwork)
            mp.put(artist_mediums, medium, medium_artworks_list)

###########################################################################################

def addNationality(catalog, artwork, data_structure):
    nationalities_map = catalog['nationalities']
    nationalities_map_keys_list = catalog['nationalities_keys']
    artists_Ids_list = GetConstituentIDList(artwork['ConstituentID'])
    for artist_Id in artists_Ids_list:
        nationality = me.getValue(mp.get(catalog['artists'], artist_Id))['info']['Nationality']
        if mp.contains(nationalities_map, nationality):
            lt.addLast(me.getValue(mp.get(nationalities_map, nationality)), artwork) 
        else:
            nationality_list = lt.newList(data_structure)
            lt.addLast(nationality_list, artwork)
            mp.put(nationalities_map, nationality, nationality_list)
            lt.addLast(nationalities_map_keys_list, nationality)

###########################################################################################

def addDepartment(catalog, artwork, data_structure):
    departments_map = catalog['departments']
    department = artwork['Department']
    if mp.contains(departments_map, department):
        lt.addLast(me.getValue(mp.get(departments_map, department)), artwork)
    else:
        department_list = lt.newList(data_structure)
        lt.addLast(department_list, artwork)
        mp.put(departments_map, department, department_list)

###########################################################################################
# Funciones para creacion de datos
###########################################################################################

def newArtist(artist, data_structure):
    artworks = lt.newList(data_structure)
    mediums = mp.newMap(50,
                    maptype='PROBING',
                    loadfactor=0.5)
    artist_info = {'info': artist,
                    'artworks': artworks,
                    'mediums': mediums}
    return artist_info

###########################################################################################
# Funciones de consulta
###########################################################################################

def getArtistsByBirthYear(catalog, data_structure, initial_birth_year, end_birth_year):
    artists_birth_years_interval = lt.newList(data_structure)
    birth_years_map = catalog['birth_years']
    for year in range(initial_birth_year, end_birth_year + 1):
        year = str(year)
        if mp.contains(birth_years_map, year):
            artists_birth_year = me.getValue(mp.get(birth_years_map, year))
            for artist in lt.iterator(artists_birth_year):
                lt.addLast(artists_birth_years_interval, artist)
    return artists_birth_years_interval

###########################################################################################

def getArtworksByAdquisitonDate(catalog, data_structure, sorting_method,
                                                    initial_adquisiton_date, end_adquisition_date):
    date_adquired_artworks_list = lt.newList(data_structure)

    adquisition_years_map = catalog['adquisition_years']
    initial_adquisition_year = getAdquisitionYear(initial_adquisiton_date)
    initial_adquisiton_date_in_days = TransformationDateToDays(initial_adquisiton_date)
    end_adquisition_year = getAdquisitionYear(end_adquisition_date)
    end_adquisition_date_in_days = TransformationDateToDays(end_adquisition_date)

    if mp.contains(adquisition_years_map, initial_adquisition_year):
        first_year_artworks = me.getValue(mp.get(adquisition_years_map, initial_adquisition_year))
        for artwork in lt.iterator(first_year_artworks):
            date = TransformationDateToDays(artwork['DateAcquired'])
            if date >= initial_adquisiton_date_in_days:
                lt.addLast(date_adquired_artworks_list, artwork)

    for year in range(initial_adquisition_year + 1, end_adquisition_year):
        if mp.contains(adquisition_years_map, year):
            year_artworks = me.getValue(mp.get(adquisition_years_map, year))
            for artwork in lt.iterator(year_artworks):
                lt.addLast(date_adquired_artworks_list, artwork)

    if mp.contains(adquisition_years_map, end_adquisition_year):
        last_year_interval_artworks = me.getValue(mp.get(adquisition_years_map, end_adquisition_year))
        for artwork in lt.iterator(last_year_interval_artworks):
            date = TransformationDateToDays(artwork['DateAcquired'])
            if date <= end_adquisition_date_in_days:
                lt.addLast(date_adquired_artworks_list, artwork)

    SortingMethodExecution(sorting_method, date_adquired_artworks_list, cmpArtworkByDateAcquired)

    return date_adquired_artworks_list


###########################################################################################
# Funciones utilizadas para comparar elementos dentro de una lista
###########################################################################################

def getDataStructure(data_structure):
    if data_structure == 1:
        data_structure_name = 'SINGLE_LINKED'
    else:
        data_structure_name = 'ARRAY_LIST'
    return data_structure_name

###########################################################################################

def getAdquisitionYear(date):
    date_information = date.split('-')
    if len(date_information) != 1:
        date_year = int(date_information[0])
    else:
        date_year = 0
    return date_year

###########################################################################################

def GetConstituentIDList(Ids_list):
    artists_list = Ids_list.strip(Ids_list[0]).strip(Ids_list[-1]).split(', ')
    return artists_list

###########################################################################################

def TransformationDateToDays(date):
    date_information = date.split('-')
    if len(date_information) != 1:
        date_in_days = int(date_information[0])*365 + int(date_information[1])*30 + int(date_information[2])
    else:
        date_in_days = 0
    return date_in_days

def getNumPurchasedArtworks(requirement_list, sorting_method):
    num_purchased_artworks = 0
    for artwork in lt.iterator(requirement_list):
        credit_line = artwork['CreditLine'].lower()
        if 'purchase' in credit_line:
            num_purchased_artworks += 1
    return num_purchased_artworks

###########################################################################################
# Funciones de ordenamiento
###########################################################################################

def SortingMethodExecution(sorting_method, list, cmpFunction):
    if sorting_method == 1:
        sorted_list = insertion.sort(list, cmpFunction)
    elif sorting_method == 2:
        sorted_list = shell.sort(list, cmpFunction)
    elif sorting_method == 3:
        sorted_list = merge.sort(list, cmpFunction)
    else:
        sorted_list = quick.sort(list, cmpFunction)

    return sorted_list

###########################################################################################
# Funciones de Comparación
###########################################################################################

def cmpArtworkByDateAcquired(artwork1, artwork2): 
    date_acquired_artwork_1 = TransformationDateToDays(artwork1['DateAcquired'])
    date_acquired_artwork_2 = TransformationDateToDays(artwork2['DateAcquired'])
    return date_acquired_artwork_1 > date_acquired_artwork_2

