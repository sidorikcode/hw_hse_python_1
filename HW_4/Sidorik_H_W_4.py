import json
import csv

# MARK: - Задания №1 + №2

class TableAgregator:
    
    def create_new_file_from_files(self, file_path_for_new_file, first_file_path: str, second_file_path: str):
        new_data = self._get_data_for_new_file(first_file_path, second_file_path)
        if new_data is not None:
             with open(file_path_for_new_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(new_data)
                return file_path_for_new_file
        else:
            return None


    def _get_data_for_new_file(self, file_path_for_txt: str, second_file_path_for_csv: str):
        source = self._get_dict_from_first_file(file_path_for_txt)
        if source is None:
            return None
    
        with open(file_path_for_second_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            colums = next(reader)
            if not len(colums) > 0:
                return None

            result_data_for_new_file = []

            for row in reader:
                try:
                    key = row[0]
                    value = source[key]
                    result_data_for_new_file.append([key, row[1], value])
                except Exception as error:
                    continue

            return result_data_for_new_file


    def _get_dict_from_first_file(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            if len(lines) <= 1:
                return None

            keys = list(json.loads(lines[0]).keys())

            if len(keys) != 2:
             return None
        
            key_for_key = keys[0]
            key_for_value = keys[1]


            result_dict = {}

            for line in lines[1:]:
                dict_whith_objects = json.loads(line)
                try:
                    new_key = dict_whith_objects[key_for_key]
                    new_value = dict_whith_objects[key_for_value]
                except Exception:
                    return None
            
                result_dict[new_key] = new_value

            return result_dict



service = TableAgregator()

file_path_for_new_file = "/Users/iliasidorik/Desktop/ВШЭ/Программирование на Python/HW_4/funnel.csv"
file_path_for_first_file = "/Users/iliasidorik/Desktop/ВШЭ/Программирование на Python/HW_4/purchase_log.txt"
file_path_for_second_file = "/Users/iliasidorik/Desktop/ВШЭ/Программирование на Python/HW_4/visit_log.csv"

new_file_path = service.create_new_file_from_files(file_path_for_new_file, file_path_for_first_file, file_path_for_second_file)