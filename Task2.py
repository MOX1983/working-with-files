import csv
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def convert_row(row, headers):
    """Конвертирует строку данных в XML элемент."""
    student = ET.Element('student')
    for i, value in enumerate(row):
        element = ET.SubElement(student, headers[i])
        element.text = value
    return student

def convert_in_xml(list):
    """Конвертирует строку данных в XML файл"""
    headers = list[0]
    root = ET.Element('students')
    for row in list[1:]:
        root.append(convert_row(row, headers))

    xml_str = ET.tostring(root)

    # Используем minidom для форматирования строки с отступами
    dom = minidom.parseString(xml_str)
    pretty_xml_as_string = dom.toprettyxml(indent="    ")
    try:
        with open("data.xml", "w") as f:
            f.write(pretty_xml_as_string)

        print("запись прошла успешно :)")
    except FileNotFoundError as ex:
        print(f"Ошибка: файл не найден - {ex}")

def convert_in_json(data_list):
    try:
        with open('data.json', 'w') as f:
            json.dump(data_list, f, indent=1)

        print("запись прошла успешно :)")
    except FileNotFoundError as ex:
        print(f"Ошибка: файл не найден - {ex}")

def convert_in_csv(data_list):
    try:
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_list)

        print("запись прошла успешно :)")
    except FileNotFoundError as ex:
        print(f"Ошибка: файл не найден - {ex}")

def reading_from_csv(string, data_list):
    if string == "1":
        try:
            with open('students.csv') as file: # для json dict
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    data_list.append(row)
                return data_list
        except FileNotFoundError as ex:
            print(f"Ошибка: файл не найден - {ex}")
    else:
        try:
            with open('students.csv') as file:# для xml list
                reader = csv.reader(file)
                for row in reader:
                    data_list.append(row)
                return data_list
        except FileNotFoundError as ex:
            print(f"Ошибка: файл не найден - {ex}")

def reading_from_json(data_list):
    try:
        with open('data.json') as file:
            rezolt = json.load(file)
            data_list.append(list(rezolt[0].keys()))
            for data in rezolt:
                data_list.append(list(data.values()))
            return data_list
    except FileNotFoundError as ex:
        print(f"Ошибка: файл не найден - {ex}")

def reading_from_xml(string, data_list):
    tree = ET.parse('data.xml')
    root = tree.getroot()

    for person in root:
        person_data = {}
        for element in person:
            person_data[element.tag] = element.text.strip() if element.text else None
        data_list.append(person_data)
    if string == "6": # для json dict
        return data_list
    else: # для csv list
        rezolt = data_list
        data_list = []
        data_list.append(list(rezolt[0].keys()))
        for data in rezolt:
            data_list.append(list(data.values()))
        return data_list

def main():
    try:
        data_list = []
        vibor = int(input("из какого формата в какой\n 1.csv --> json\n 2.csv --> xml\n 3.json --> csv\n 4.json --> xml \n 5.xml --> csv\n 6.xml --> json\n"))
        match vibor:
            case 1:
                reading_from_csv("1", data_list)
                convert_in_json(data_list)
            case 2:
                reading_from_csv("2", data_list)
                convert_in_xml(data_list)
            case 3:
                reading_from_json(data_list)
                convert_in_csv(data_list)
            case 4:
                reading_from_json(data_list)
                convert_in_xml(data_list)
            case 5:
                convert_in_csv(reading_from_xml("5", data_list))
            case 6:
                reading_from_xml("6", data_list)
                convert_in_json(data_list)
    except Exception as ex:
        print(ex)

if __name__=="__main__":
    main();

# Name,Surname,Age,Group,Average-score
# Izmailov,Arseniy,19,isit,8.8
# Chernaya,Anastasia,21,pi,8.9
# Popova,Lidiya,19,fmo,7.6
# Dmitrieva,Darina,21,uir,6.4
# Moskvin,Vladimir,21,isit,6.7
# Dmitriev,Ilya,18,pi,9.8
# Golubev,Vladislav,18,fmo,5.2
# Nikitin,Makar,19,uir,7.9
# Sidorov,Artem,20,isit,8.0
# Savina,Daria,18,pi,7.0

# [
#  {
#   "Name": "Izmailov",
#   "Surname": "Arseniy",
#   "Age": "19",
#   "Group": "isit",
#   "Average-score": "8.8"
#  },
#  {
#   "Name": "Chernaya",
#   "Surname": "Anastasia",
#   "Age": "21",
#   "Group": "pi",
#   "Average-score": "8.9"
#  },
#  {
#   "Name": "Popova",
#   "Surname": "Lidiya",
#   "Age": "19",
#   "Group": "fmo",
#   "Average-score": "7.6"
#  },
#  {
#   "Name": "Dmitrieva",
#   "Surname": "Darina",
#   "Age": "21",
#   "Group": "uir",
#   "Average-score": "6.4"
#  },
#  {
#   "Name": "Moskvin",
#   "Surname": "Vladimir",
#   "Age": "21",
#   "Group": "isit",
#   "Average-score": "6.7"
#  },
#  {
#   "Name": "Dmitriev",
#   "Surname": "Ilya",
#   "Age": "18",
#   "Group": "pi",
#   "Average-score": "9.8"
#  },
#  {
#   "Name": "Golubev",
#   "Surname": "Vladislav",
#   "Age": "18",
#   "Group": "fmo",
#   "Average-score": "5.2"
#  },
#  {
#   "Name": "Nikitin",
#   "Surname": "Makar",
#   "Age": "19",
#   "Group": "uir",
#   "Average-score": "7.9"
#  },
#  {
#   "Name": "Sidorov",
#   "Surname": "Artem",
#   "Age": "20",
#   "Group": "isit",
#   "Average-score": "8.0"
#  },
#  {
#   "Name": "Savina",
#   "Surname": "Daria",
#   "Age": "18",
#   "Group": "pi",
#   "Average-score": "7.0"
#  }
# ]

# <?xml version="1.0" ?>
# <students>
#     <student>
#         <Name>Izmailov</Name>
#         <Surname>Arseniy</Surname>
#         <Age>19</Age>
#         <Group>isit</Group>
#         <Average-score>8.8</Average-score>
#     </student>
#     <student>
#         <Name>Chernaya</Name>
#         <Surname>Anastasia</Surname>
#         <Age>21</Age>
#         <Group>pi</Group>
#         <Average-score>8.9</Average-score>
#     </student>
#     <student>
#         <Name>Popova</Name>
#         <Surname>Lidiya</Surname>
#         <Age>19</Age>
#         <Group>fmo</Group>
#         <Average-score>7.6</Average-score>
#     </student>
#     <student>
#         <Name>Dmitrieva</Name>
#         <Surname>Darina</Surname>
#         <Age>21</Age>
#         <Group>uir</Group>
#         <Average-score>6.4</Average-score>
#     </student>
#     <student>
#         <Name>Moskvin</Name>
#         <Surname>Vladimir</Surname>
#         <Age>21</Age>
#         <Group>isit</Group>
#         <Average-score>6.7</Average-score>
#     </student>
#     <student>
#         <Name>Dmitriev</Name>
#         <Surname>Ilya</Surname>
#         <Age>18</Age>
#         <Group>pi</Group>
#         <Average-score>9.8</Average-score>
#     </student>
#     <student>
#         <Name>Golubev</Name>
#         <Surname>Vladislav</Surname>
#         <Age>18</Age>
#         <Group>fmo</Group>
#         <Average-score>5.2</Average-score>
#     </student>
#     <student>
#         <Name>Nikitin</Name>
#         <Surname>Makar</Surname>
#         <Age>19</Age>
#         <Group>uir</Group>
#         <Average-score>7.9</Average-score>
#     </student>
#     <student>
#         <Name>Sidorov</Name>
#         <Surname>Artem</Surname>
#         <Age>20</Age>
#         <Group>isit</Group>
#         <Average-score>8.0</Average-score>
#     </student>
#     <student>
#         <Name>Savina</Name>
#         <Surname>Daria</Surname>
#         <Age>18</Age>
#         <Group>pi</Group>
#         <Average-score>7.0</Average-score>
#     </student>
# </students>
