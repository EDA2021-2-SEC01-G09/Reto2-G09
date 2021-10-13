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

# Construccion de modelos

def newCatalog():
    catalog = {'artworks': None,
               'artworkIds': None,
               'artists': None,
               'artistIds': None,
               'mediumIds': None,
               'nationalityIds': None}
 
    catalog['artworks'] = lt.newList('SINGLE_LINKED', compareArtworkandArtistIds)
    catalog['artworkIds'] = mp.newMap(1543,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapArtworkandArtistIds)
    catalog['artists'] = lt.newList('SINGLE_LINKED', compareArtworkandArtistIds)
    catalog['artistIds'] = mp.newMap(3907,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapArtworkandArtistIds)
    catalog['mediumIds'] = mp.newMap(768,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    catalog['nationalityIds'] = mp.newMap(101,
                                   maptype='PROBING',
                                   loadfactor=0.5)

    return catalog

def newArtworkMedium(name, first_artwork):
    medium = {'name': '',
           'total_artworks': 1,
           'artworks': None,}
    medium['name'] = name
    medium['artworks'] = lt.newList()
    lt.addLast(medium['artworks'], first_artwork)
    return medium

def newArtworkNationality(name, first_artwork):
    Nationality = {'name': '',
           'total_artworks': 1,
           'artworks': None,}
    Nationality['name'] = name
    Nationality['artworks'] = lt.newList()
    lt.addLast(Nationality['artworks'], first_artwork)
    return Nationality

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    mp.put(catalog['artworkIds'], artwork['ObjectID'], artwork)
    
def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)
    mp.put(catalog['artistIds'], artist['ConstituentID'], artist)

def addMedium(catalog, medium, artwork):
    if mp.contains(catalog['mediumIds'],medium) == False:
        mp.put(catalog['mediumIds'], medium, newArtworkMedium(medium, artwork))     
    else:
        artworks_list_medium = me.getValue(mp.get(catalog['mediumIds'], medium))['artworks']
        lt.addLast(artworks_list_medium, artwork)
        me.getValue(mp.get(catalog['mediumIds'], medium))['total_artworks'] += 1

def addNationality(catalog, artistIds_list, artwork):
    for artistId in artistIds_list:
        nationality = mp.get(catalog['artistIds'], artistId)['value']['Nationality']
        if mp.contains(catalog['nationalityIds'], nationality) == False:
            mp.put(catalog['nationalityIds'], nationality, newArtworkNationality(nationality, artwork))     
        else:
            artworks_list_nationality = me.getValue(mp.get(catalog['nationalityIds'], nationality))['artworks']
            lt.addLast(artworks_list_nationality, artwork)
            me.getValue(mp.get(catalog['nationalityIds'], nationality))['total_artworks'] += 1

# Funciones para creacion de datos

# Funciones de consulta

def artworksSize(catalog):
    return mp.size(catalog['artworks'])

def artistsSize(catalog):
    return mp.size(catalog['artists'])

def mediumsSize(catalog):
    return mp.size(catalog['mediumIds'])

def nationalitiesSize(catalog):
    return mp.size(catalog['nationalityIds'])

def getArtworksByNationality(catalog, nationality, num_artworks):
    nationality_artworks = mp.get(catalog['nationalityIds'], nationality)['value']['artworks'].copy()
    num_nationality = mp.get(catalog['nationalityIds'],nationality)['value']['total_artworks']
    sublist_nationality_artworks = lt.subList(nationality_artworks, num_nationality - num_artworks, num_artworks)
    return sublist_nationality_artworks, num_nationality

def GetConstituentIDListArtwork(artwork):
    ID = artwork['ConstituentID']
    artwork_constituent_IDs = ID.strip(ID[0]).strip(ID[-1]).split(', ')
    return artwork_constituent_IDs

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def getOlderArtworksByMedium(catalog, medium, num_artworks):
    medium_artworks = mp.get(catalog['mediumIds'],medium)['value']['artworks'].copy()
    merge.sort(medium_artworks, cmpDateArtworks)
    older_medium_artworks = lt.subList(medium_artworks, lt.size(medium_artworks) - num_artworks, num_artworks)
    return older_medium_artworks

# Funciones de Comparación

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