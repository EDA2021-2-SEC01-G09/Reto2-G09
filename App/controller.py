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
import time
#import psutil

###########################################################################################
# Inicialización del Catálogo de libros
###########################################################################################

def initCatalog(data_structure):
    start_time = time.process_time()

    catalog = model.newCatalog(data_structure)

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000  
    #RAM_usage = psutil.virtual_memory()[2]
    RAM_usage = 0
    return elapsed_time, RAM_usage, catalog

###########################################################################################
# Funciones para la carga de datos
###########################################################################################

def loadData(initiation_data, data_structure, artists_sample_size, artworks_sample_size):
    start_time = time.process_time()

    loadArtistsRelatedData(initiation_data, data_structure, artists_sample_size)
    loadArtworksRelatedData(initiation_data, data_structure, artworks_sample_size)
    
    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000  
    #RAM_usage = psutil.virtual_memory()[2]
    RAM_usage = 0
    return elapsed_time, RAM_usage

###########################################################################################

def loadArtistsRelatedData(catalog, data_structure, sample_size):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    artists_info = list(input_file)[:sample_size]
    for artist in artists_info:
        model.addArtist(catalog, artist, data_structure)
        model.addBirthYearArtist(catalog, artist, data_structure)
    
###########################################################################################

def loadArtworksRelatedData(catalog, data_structure, sample_size):
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    artworks_info = list(input_file)[:sample_size]
    for artwork in artworks_info:
        model.addArtwork(catalog, artwork)
        model.addAdquisitionYear(catalog, artwork, data_structure)
        model.addMedium(catalog, artwork, data_structure)
        model.addNationality(catalog, artwork, data_structure)
        model.addDepartment(catalog, artwork, data_structure)

###########################################################################################
# Funciones de ordenamiento
###########################################################################################

###########################################################################################
# Funciones de consulta sobre el catálogo
###########################################################################################

def getDataStructure(data_structure):
    return model.getDataStructure(data_structure)

###########################################################################################

def getArtistsByBirthYear(catalog, data_structure, initial_birth_year, end_birth_year):
    start_time = time.process_time()

    requirement_list = model.getArtistsByBirthYear(catalog, data_structure,
                                                     initial_birth_year, end_birth_year)

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000  
    #RAM_usage = psutil.virtual_memory()[2]
    RAM_usage = 0
    return elapsed_time, RAM_usage, requirement_list