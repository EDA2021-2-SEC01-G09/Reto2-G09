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
 """

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtworks(catalog)
    loadArtists(catalog)
    loadMediums(catalog)
    loadNationalities(catalog)

def loadArtworks(catalog):
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def loadArtists(catalog):
    artworksfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtist(catalog, artwork)

def loadMediums(catalog):
    for artwork in lt.iterator(catalog['artworks']):
        medium = artwork['Medium']
        model.addMedium(catalog, medium, artwork)

def loadNationalities(catalog):
    for artwork in lt.iterator(catalog['artworks']):
        artistIds_list = GetConstituentIDListArtwork(artwork)
        model.addNationality(catalog, artistIds_list, artwork)


# Funciones de ordenamiento

def getOlderArtworksByMedium(catalog, medium, num_artworks):
    return model.getOlderArtworksByMedium(catalog, medium, num_artworks)

def getArtworksByNationality(catalog, nationality, num_artworks):
    return model.getArtworksByNationality(catalog, nationality, num_artworks)

# Funciones de consulta sobre el catálogo

def artworksSize(catalog):
    return model.artworksSize(catalog)

def artistsSize(catalog):
    return model.artistsSize(catalog)

def mediumsSize(catalog):
    return model.mediumsSize(catalog)
    
def nationalitiesSize(catalog):
    return model.nationalitiesSize(catalog)

def GetConstituentIDListArtwork(artwork):
    return model.GetConstituentIDListArtwork(artwork)