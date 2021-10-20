import config as cf
import sys
import controller
import xlsxwriter
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def TestFunction(catalog, option, data_structure, sorting_method, input_1, input_2, input_3):
    if option == 1:
        artists_sample_size = input_1
        artworks_sample_size = input_2
        catalog = controller.initCatalog(data_structure)
        controller.loadData(catalog, data_structure, artists_sample_size, artworks_sample_size)
        result = catalog

    elif option == 2:
        initial_birth_year = input_1
        end_birth_year = input_2
        requirement_info = controller.getArtistsByBirthYear(catalog, data_structure,
                                                                initial_birth_year, end_birth_year)
        elapsed_time = requirement_info[0]
        RAM_used = requirement_info[1]
        result = elapsed_time, RAM_used

    elif option == 3:
        initial_adquisiton_date = input_1
        end_adquisition_date = input_2
        requirement_info = controller.getArtworksByAdquisitonDate(catalog, data_structure, sorting_method,
                                                        initial_adquisiton_date, end_adquisition_date)
        elapsed_time = requirement_info[0]
        RAM_used = requirement_info[1]
        result = elapsed_time, RAM_used

    elif option == 4:
        artist_name = input_1
        requirement_info = controller.getArtworksByMediumAndArtist(catalog, artist_name)
        elapsed_time = requirement_info[0]
        RAM_used = requirement_info[1]
        result = elapsed_time, RAM_used

    elif option == 5:
        requirement_info = controller.getNationalitiesByNumArtworks(catalog, data_structure, sorting_method)
        elapsed_time = requirement_info[0]
        RAM_used = requirement_info[1]
        result = elapsed_time, RAM_used

    elif option == 6:  
        department = input_1
        requirement_info = controller.getTransportationCostByDepartment(catalog, data_structure, 
                                                                                sorting_method, department)
        elapsed_time = requirement_info[0]
        RAM_used = requirement_info[1]
        result = elapsed_time, RAM_used

    else:
        num_artists = input_1
        initial_birth_year = input_2
        end_birth_year = input_3
        requirement_info = controller.getMostProlificArtists(catalog, data_structure, sorting_method,
                                                                    initial_birth_year, end_birth_year, num_artists)
        elapsed_time = requirement_info[0]
        RAM_used = requirement_info[1]
        result = elapsed_time, RAM_used
    return result

def InitiateFunction():
    requeriment_test = {    2: (1900, 1905, 0),
                            3: ('1985-01-01', '2000-01-01', 0),
                            4: ('Alexei Jawlensky', 0, 0),
                            5: (0, 0, 0),
                            6: ('Drawings & Prints', 0, 0),
                            7: (3, 1900, 1905)}
    data_structure_test = { (1523, 1382):requeriment_test,
                            (3045, 2763):requeriment_test,
                            (4567, 4144):requeriment_test,
                            (6089, 5525):requeriment_test,
                            (7611, 6906):requeriment_test,
                            (9134, 8287):requeriment_test,
                            (10656, 9668):requeriment_test,
                            (12178, 11049):requeriment_test}
    Test_Data = {   'SINGLE_LINKED':data_structure_test,
                    'ARRAY_LIST':data_structure_test}


    workbook   = xlsxwriter.Workbook('Test_Data.xlsx')
    worksheet = workbook.add_worksheet()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    initial_x_position_time = 0
    initial_x_position_RAM = 10
    for data_structure in Test_Data:
        data_structure_info = Test_Data[data_structure]
        initial_y_position = -9
        for sample in data_structure_info:
            input_1 = sample[0]
            input_2 = sample[1]
            catalog = TestFunction(None, 1, data_structure, 0, input_1, input_2, 0)
            sample_info = data_structure_info[sample]
            initial_y_position += 1
            y_position = initial_y_position
            for requirement in sample_info:
                inputs = sample_info[requirement]
                input_1 = inputs[0]
                input_2 = inputs[1]
                input_3 = inputs[2]
                y_position += 9
                x_position_time = initial_x_position_time
                x_position_RAM = initial_x_position_RAM
                for sorting_method in range(1,5):
                    x_position_time += 1 
                    x_position_RAM += 1
                    position_time_index = alphabet[x_position_time - 1] + str(y_position)
                    position_RAM_index = alphabet[x_position_RAM - 1] + str(y_position)
                    elapsed_time = 0
                    RAM_used = 0
                    for i in range(0,3):
                        test_info = TestFunction(catalog, requirement, data_structure, sorting_method, input_1, input_2, input_3)
                        test_time = test_info[0]
                        test_RAM = test_info[1]
                        elapsed_time += test_time
                        RAM_used += test_RAM
                        mean_elapsed_time = round(elapsed_time/3, 2)
                        mean_RAM_used = round(RAM_used/3, 2)
                        worksheet.write(position_time_index, mean_elapsed_time)
                        worksheet.write(position_RAM_index, mean_RAM_used)      
        initial_x_position_time += 5
        initial_x_position_RAM += 5
    workbook.close()

InitiateFunction()