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
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ Inicializa el catálogo de obras

    Crea una lista vacia para guardar todos las obras

    Se crean indices (Maps) por los siguientes criterios:
    Obras
    Medios

    Retorna el catalogo inicializado.
    """
    catalog = {'artworks': None,
               'artworkIds': None,}
    """
    Esta lista contiene todo las obras encontradas
    en los archivos de carga.  Estas obras no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['artworks'] = lt.newList('SINGLE_LINKED', compareArtworkIds)
    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian las obras de la lista
    creada en el paso anterior.
    """

    """
    Este indice crea un map cuya llave es el identificador de la obra
    """
    catalog['artworkIds'] = mp.newMap(250,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapArtworkIds)
    """
    Este indice crea un map cuya llave es el medio
    """

    return catalog

def newArtworkMedium(name, id):
    """
    Esta estructura crea una relación entre un medium y las obras
    hechas en dicho medium. Se guarga el total de obras y una lista con
    dichas obras.
    """
    medium = {'name': '',
           'medium_id': '',
           'total_artworks': 0,
           'artworks': None,
           'count': 0.0}
    medium['name'] = name
    medium['medium_id'] = id
    medium['artworks'] = lt.newList()
    return medium
    

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    """
    Esta funcion adiciona una obra a la lista de obras,
    adicionalmente lo guarda en un Map usando como llave su Id.
    """
    lt.addLast(catalog['artworks'], artwork)
    mp.put(catalog['artworkIds'], artwork['ObjectID'], artwork)
    

# Funciones para creacion de datos

# Funciones de consulta

def artworksSize(catalog):
    """
    Numero de obras cargados al catalogo
    """
    return mp.size(catalog['artworks'])


# Funciones utilizadas para comparar elementos dentro de una lista

def getArtworksByMedium(artworkIds, medium):
    medium_artworks = mp.newMap(1600,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    for artwork in artworkIds:
        artwork_medium = me.getValue(artwork)['Medium']
        if artwork_medium == medium:
            artwork_Id = me.getValue(artwork)['ObjectID']
            mp.put(medium_artworks,artwork_Id,artwork)
    return medium_artworks

def getnOlderArtworks(medium_artworks,num_artworks):
    return None


# Funciones de ordenamiento

# Funciones de Comparación

def compareArtworkIds(id1, id2):
    """
    Compara dos ids de dos libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapArtworkIds(id, entry):
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