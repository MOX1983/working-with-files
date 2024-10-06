import csv

try:
    with open('students.csv') as file:
        try:
            csv_reader = csv.DictReader(file)
            data_list = []

            for row in csv_reader:
                data_list.append(row)

            for data in data_list:
                print(data)

            print('')

            sorted_list = sorted(data_list, key=lambda x: x['Average-score']) #,reverse=True если в другую сторону надо :)
            for data in sorted_list:
                print(data)

            print('')

            print('возраст в группе')
            for group in ['isit', "pi", "fmo", 'uir']:
                sum = 0
                counter = 0
                for data in data_list:
                    if data['Group'] in group:
                        sum += int(data['Age'])
                        counter += 1
                print(f"{group}: {sum / counter}")

            print('')

            limit = float(input("Введите лимит средниего балла:"))
            for data in data_list:
                if float(data['Average-score']) > limit:
                    print(data["Name"], data["Surname"])

        except Exception as ex:
            print(ex)
except FileNotFoundError as ex:
    print(f"Ошибка: файл не найден - {ex}")