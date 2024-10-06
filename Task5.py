import json
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
while True:
    try:
        fail = input("название файла ")
        with open(fail) as file:
            rezolt = json.load(file)
            data_list = []
            for data in rezolt:
                data_list.append(data)
    except FileNotFoundError as ex:
        logging.error(ex)

    try:
        print(int(input("введите ЦИФРЫ!!! ")))
    except Exception as ex:
        logging.error(ex)