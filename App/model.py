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

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merge
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
# Funciones utilizadas para comparar elementos dentro de una lista
###########################################################################################

###########################################################################################
# Funciones de ordenamiento
###########################################################################################

###########################################################################################
# Funciones de Comparación
###########################################################################################

def compareArtworkandArtistIds(id1, id2):
    """
    Compara dos ids de dos libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapArtworkandArtistIds(id, entry):
    """
    Compara dos ids de obras, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def cmpDateArtworks(artwork1, artwork2):
    artwork1_date = artwork1['Date']
    artwork2_date = artwork2['Date']
    if artwork1_date == '':
        artwork1_date = 0
    if artwork2_date == '':
        artwork2_date = 0 
 
    return artwork1_date > artwork2_date