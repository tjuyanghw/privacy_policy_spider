from fuzzywuzzy import fuzz
from terminaltables import AsciiTable
import os
import numpy as np
import difflib
import sys


def main():
    if len(sys.argv) <= 1:
        #print("Test")
        return

    folder_location = sys.argv[1]
    print(folder_location)
    if not os.path.isdir(folder_location):
        print("Wrong directory! " + folder_location)
        return

    all_files = os.listdir(folder_location)
    total_length = len(all_files)

    if total_length <= 1:
        print("The directory has to contain two or more files to be compared!")
        return

    similarity_list = np.zeros((total_length, total_length))
    files_content = ["" for x in range(len(all_files))]
    # print(similarity_list.shape)

    # <editor-fold desc="Reading all the files into the memory" >
    for i, file in enumerate(all_files):
        text = open(folder_location + "\\" + file, 'r').read()
        files_content[i] = text
    # print(files_content[1])
    # </editor-fold >

    # <editor-fold desc="Filling percentages" >

    for i in range(0, total_length):
        print("Processing file (", i+1, " / ", total_length, ")..")
        for j in range(i+1, total_length):
            # percentage = 0
            percentage = fuzz.ratio(files_content[i], files_content[j])
            percentage += round(difflib.SequenceMatcher(None, files_content[i], files_content[j]).ratio()*100)
            percentage /= 2
            # if percentage > 25:
            similarity_list[i, j] = similarity_list[j, i] = percentage
    # </editor-fold >

    # <editor-fold desc="Printing as similarity percentages as table" >
    print("Result: ")
    table_data_length = total_length + 1
    table_data = [["" for x in range(table_data_length)] for y in range(table_data_length)]
    for i, file in enumerate(all_files):
        table_data[0][i + 1] = file
        table_data[i + 1][0] = file

        for index, val in enumerate(similarity_list[i]):
            table_data[i + 1][index + 1] = val
    table = AsciiTable(table_data)
    print(table.table)

    result_file_name = "result.txt"
    file = open(result_file_name, 'w')
    file.write(table.table)
    file.close()
    print("Table has been written in " + result_file_name)
    # </editor-fold>

    pass

if __name__ == '__main__':
    main()
