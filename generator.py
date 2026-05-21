# Script by Tamás Dékány

def loader(input_file_name):
    try:
        with open(input_file_name, "r") as f:
            lines = f.readlines()
        return lines
    except TypeError:
        print("Wrong file name!\n")
    except FileNotFoundError:
        print("File not found/File with wrong extension!\n")
    return None

def file_path_adder(file_type):
    file_path = ""
    
    if file_type == "hap":
        file_path = input(" Hap file: ") + ".txt"
    if file_type == "id":
        file_path = input(" ID file:  ") + ".txt"
    if file_path == "" or file_path is None or ".txt.txt" in file_path in file_path:
        return None
    return file_path

def id_to_dict(id_file):
    dict_id = dict()
    country_set = set()
    firstline = True
    duplicate_ids = 0
    duplicate_string_list = []
    duplicate_string = ""
    
    for row in id_file:
        if firstline or row.isspace():
            firstline = False
            continue
        
        row_list = row.split()
        country_name= ""
        for i in range(len(row_list)):
            if i == 0:
                continue
            country_name += row_list[i]
            if i != len(row_list)-1:
                country_name += " "
        country_set.add(country_name)
        
        if row_list[0] in dict_id:
            duplicate_ids += 1
            duplicate_string_list.append(row_list[0])
        else:    
            dict_id[row_list[0]] = country_name
    
    country_list = list(country_set)
    country_list.sort()  
    if len(duplicate_string_list) > 0:
        duplicate_string = ", ".join(duplicate_string_list)
    return dict_id, country_list, duplicate_ids, duplicate_string

def hap_to_dict(hap_file):  
    hap_elements = 0
    
    try:
        dict_hap = {}
        for row in hap_file:
            if "Hap#" in row or row.isspace():
                continue
            list_row = row.split()
            str_type = list(list_row[0])
            str_type.pop(0)
            str_type.pop(len(str_type) - 1)
            list_row[0] = ''.join(str_type)

            hap_freq_list = []
            for i in range(int(list_row[1])):
                hap_freq_list.append(list_row[i + 2])
            hap_freq_list[len(hap_freq_list) - 1] = hap_freq_list[len(hap_freq_list) - 1][:-1]
            dict_hap[list_row[0]] = hap_freq_list
            hap_elements += len(hap_freq_list)
        return dict_hap, hap_elements
    except Exception:
        return None

if __name__ == "__main__":
    hap_file_loaded = False
    id_file_loaded = False
    
    print("Enter the file's name/path without the '.txt' extension")
    while not (hap_file_loaded and id_file_loaded):
        if not hap_file_loaded:
            hap_file = loader(file_path_adder("hap"))
            if hap_file is not None:
                hap_file_loaded = True
        if not id_file_loaded:
            id_file = loader(file_path_adder("id"))
            if id_file is not None:
                id_file_loaded = True
    
    print("...Files are loaded...\n")
    id_dict, country_list, duplicate_ids, duplicate_string = id_to_dict(id_file)  
    
    try:
        hap_dict, hap_elements = hap_to_dict(hap_file)
    except TypeError:
        print("Please, check the format of the 'hap' file and reload the script!")
        exit()
    
    if (duplicate_ids > 0):
        print("Found duplication in id file! The list of duplications:\n " + duplicate_string)
    if len(id_dict) != hap_elements:
        if len(id_dict) > hap_elements:
            type_str = "id "
        else:
            type_str = "hap"
        print("The " + type_str + " file has more elements!")


    try:    
        output_table = [["" for _ in range(len(country_list) + 1)] for _ in range(len(hap_dict) + 1)]
        for i in range(len(output_table)):
            if i == 0:
                for j in range(len(country_list)):
                    output_table[i][j+1] = (country_list[j])
                    if j != len(country_list)-1:
                        output_table[i][j+1] += ","
            else:
                key = "Hap_" + str(i)
                output_table[i][0] = key + ","
                for j in range(len(country_list)):
                    output_table[i][j+1] = "0,"
                temp_dict = dict()
                for seq in hap_dict[key]:
                    if seq not in id_dict:
                        temp_key = seq[:-2]
                    else:
                        temp_key = seq

                    if id_dict[temp_key] in temp_dict:
                        temp_dict[id_dict[temp_key]] += 1
                    else:
                        temp_dict[id_dict[temp_key]] = 1
                for key in temp_dict:
                    table_index = country_list.index(key)
                    output_table[i][table_index+1] = str(temp_dict[key]) + ","
                    
    except TypeError:
        print("Please, check the format of the 'hap' file and reload the script!")
        exit()
        
    except KeyError as e:
        print("The id in the hap file - starting with/called - " + str(e) + " is - different/not found - in the id file!")
    
    except Exception:
        print("Please, check the format of the 'id' file and reload the script!")
        exit()

    output = [""]
    for i in range(len(output_table)):
        if i == 0:
            row = "".join(output_table[i])
        else:
            row = "\t".join(output_table[i])
        if i != len(output_table) - 1:
            row += "\n"
        output.append(row)
    with open("output.txt", "w") as f:
       f.writelines(output)

    print("The output is written to 'output.txt'")